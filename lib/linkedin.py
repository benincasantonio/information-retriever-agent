import json
import requests
import os


def scrape_linkedin_profile(url: str, mock: bool = False) -> dict:

    if mock:
        with open("assets/linkedin_mock.json", "r") as f:
            data = json.load(f).get("person", {})

    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"

        params = {
            "apikey": os.getenv("SCRAPIN_API_KEY"),
            "linkedInUrl": url,
        }

        response = requests.get(api_endpoint, params=params, timeout=10)

        data = response.json().get("person", {})

    return clean_empty_fields(data)


def clean_empty_fields(data: dict) -> dict:
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            if key.endswith("Count") and value == 0:
                continue
            elif isinstance(value, (dict, list)):
                cleaned_value = clean_empty_fields(value)
                if cleaned_value not in (None, {}, []):
                    new_dict[key] = cleaned_value
            elif value not in (None, "", []):
                new_dict[key] = value
        return new_dict

    elif isinstance(data, list):
        return [
            clean_empty_fields(item)
            for item in data
            if clean_empty_fields(item) not in (None, {}, [])
        ]

    return data
