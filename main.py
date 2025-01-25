from os import environ
from openai import OpenAI
from dotenv import load_dotenv
from flask import jsonify

load_dotenv()

OPENAI_API_KEY = environ["OPENAI_API_KEY"]

client = OpenAI()

def get_output(num_restaurants, location, cuisine, radius_mi):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=150,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "list " + str(num_restaurants) + " " + cuisine + " restaurants in " + location + " within a " + str(radius_mi) + " mile radius."
            }
        ],
    )
    return response.choices[0].message.content

print(get_output(5, "seattle", "asian", 3))