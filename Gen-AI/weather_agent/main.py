from google import genai
from dotenv import load_dotenv
import requests
load_dotenv()

client = genai.Client()

def get_wateher(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%c+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong"

def main():
    user_query = input("> ")

    response = client.interactions.create(
        model="gemini-3.7-flash",
        input=user_query
    )

    print(f"🤖: {response.output_text}")

main()
