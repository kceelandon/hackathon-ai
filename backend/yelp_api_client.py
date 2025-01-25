import requests
from os import environ
from dotenv import load_dotenv

load_dotenv()

YELP_API_KEY = environ.get("YELP_API_KEY")

def get_data_from_yelp(params):
    location = params["location"]
    term = params["name"]
    base_endpoint = "https://api.yelp.com/v3"
    url = base_endpoint + f"/businesses/search?location={location}&term="
    search_term_url = ""
    split_text = term.split(" ")
    for i in range(len(split_text)):
        if i == len(split_text) - 1:
            search_term_url += split_text[i]
        else:
            search_term_url += split_text[i] + "%20"
    url += search_term_url + "&sort_by=best_match&limit=20"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {YELP_API_KEY}"
    }
    response = requests.get(url=url, headers=headers)
    return response.json()

test_object = {"location": "Seattle", "name": "Din Tai Fung"}

print(get_data_from_yelp(test_object)["businesses"][0])