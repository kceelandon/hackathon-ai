from os import environ
from openai import OpenAI
from dotenv import load_dotenv
app = Flask(__name__)
load_dotenv()


OPENAI_API_KEY = environ["OPENAI_API_KEY"]
client = OpenAI()

def chat():
    print("Welcome to the Chatbot! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=150,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
        )
        print("Bot:", response.choices[0].message.content)

chat()