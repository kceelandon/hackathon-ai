from flask import Flask # type: ignore
from flask import jsonify, request  # type: ignore
from os import environ
from openai import OpenAI # type: ignore
from dotenv import load_dotenv # type: ignore
from flask_cors import CORS # type: ignore
import yelp_api_client
app = Flask(__name__)
CORS(app)


load_dotenv()

OPENAI_API_KEY = environ["OPENAI_API_KEY"]

client = OpenAI()

def extract_restaurant_names(text):
    # Split the text by newline characters
    lines = text.split('\n')
    # Extract the restaurant names by splitting each line at the ". " and taking the second part
    restaurant_names = [line.split('. ')[1] for line in lines if '. ' in line]
    return restaurant_names

@app.route('/findfood', methods=['POST'])
def get_output():
    data = request.get_json()
    print(data)
    num_restaurants = data['numRestaurants']
    cuisine = data["cuisine"]
    location = data["city"]
    radius_mi = data["radius"]
    lol = f"please list only the names of {num_restaurants} {cuisine} restaurants in {location} within a {radius_mi} mile radius. nothign else"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=150,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": lol,
            }
        ],
    )
    restaurant_names = extract_restaurant_names(response.choices[0].message.content)
    data = []
    for name in restaurant_names:
        params = {"location": location, "name": name}
        data.append(yelp_api_client.get_data_from_yelp(params=params)["businesses"][0])
        # appends yelp data
    lol = {
        "data": data
    }
    return jsonify(lol)




if __name__ == '__main__':
    app.run(debug=True)
