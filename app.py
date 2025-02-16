from lib.retrieve_information import retrieve_information
import streamlit as st

from parsers.summary_parser import Summary

if __name__ == "__main__":
    name = st.text_input("Enter name")
    button = st.button("Submit")

    if button and name:
        with st.spinner('Retrieving Information...'):
            result = retrieve_information(name=name, mock=True)
        summary: Summary = result[0]
        image_url: str = result[1]

        st.html(f'<img src="{image_url}" width="200" style="border-radius: 50%;">')

        st.header("Summary")
        st.text(summary.summary)

        st.header("Interesting Facts")

        for fact in summary.facts:
            st.text(fact)


