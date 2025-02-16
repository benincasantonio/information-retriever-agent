# Information Retriever Agent

## Overview

This project is an Information Retriever Agent that uses LinkedIn data to provide a summary and interesting facts about a person. The application is built using Python and leverages various libraries and APIs to achieve its functionality.

## Project Structure

```
agents/
	__init__.py
	search_linkedin_agent.py
app.py
assets/
	linkedin_mock.json
lib/
	__init__.py
	linkedin.py
	retrieve_information.py
parsers/
	__init__.py
	summary_parser.py
requirements.txt
tools/
	__init__.py
	linkedin_url_search_tool.py
```

## Requirements

The project dependencies are listed in the `requirements.txt` file. To install them, run:

```sh
pip install -r requirements.txt
```

## Setup
To set up the project, follow these steps:

1. **Create a virtual environment**

```sh
python3 -m venv .venv
```

2. **Activate the virtual environment**

- On macOS and Linux:

```sh
source .venv/bin/activate
```

- On Windows:

```sh
.venv\Scripts\activate
```

3. **Install the project dependencies**

```sh
pip install -r requirements.txt
```

## Environment Variables

The project requires the following environment variables, which should be defined in a `.env` file:

| Variable Name      | Description                          |
|--------------------|--------------------------------------|
| `SCRAPIN_API_KEY`  | API key for Scrapin.io               |
| `TAVILY_API_KEY`   | API key for Tavily                   |
| `GOOGLE_API_KEY`   | API key for Google                   |

## Usage

To run the application, execute the following command:

```sh
streamlit run app.py
```

## Models and APIs

The application uses the following models and APIs:

- **phi4 model**: Used to summarize the information. More details can be found [here](https://ollama.com/library/phi4).
- **Gemini API**: Used for the search LinkedIn agent.

These models and APIs can easily be changed thanks to the flexibility provided by LangChain.

## Files Description

- `agents/search_linkedin_agent.py`: Contains the agent logic to search for LinkedIn profiles.
- `app.py`: The main application file that runs the Streamlit app.
- `assets/linkedin_mock.json`: Mock data for LinkedIn profiles.
- `lib/linkedin.py`: Functions to scrape LinkedIn profiles.
- `lib/retrieve_information.py`: Functions to retrieve information and generate summaries.
- `parsers/summary_parser.py`: Parser for the summary and interesting facts.
- `tools/linkedin_url_search_tool.py`: Tool to search for LinkedIn URLs using Tavily.

## License

This project is licensed under the MIT License.
