from flask import Flask # type: ignore
from flask import jsonify, request  # type: ignore
from os import environ
from openai import OpenAI # type: ignore
from dotenv import load_dotenv # type: ignore
app = Flask(__name__)



load_dotenv()

OPENAI_API_KEY = environ["OPENAI_API_KEY"]

client = OpenAI()

@app.route('/findfood', methods=['POST'])
def get_output():
    data = request.get_json()
    print(data)
    num_restaurants = 4
    cuisine = "asian"
    location = "seattle"
    radius_mi = 4
    lol = f"please list only the names of {num_restaurants} {cuisine} restaurants in {location} within a {radius_mi} mile radius. nothign else just names give me the name in a array of strings"
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
    data = {
        "message": response.choices[0].message.content
    }
    return  jsonify(data)




if __name__ == '__main__':
    app.run(debug=True)
