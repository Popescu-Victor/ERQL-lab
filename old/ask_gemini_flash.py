import os
from dotenv import load_dotenv
import google.generativeai as genai


def main(question: str):
    load_dotenv() 
    api_key = os.getenv("GEMINI_API_KEY")

    if api_key is None:
        raise ValueError("GEMINI_API_KEY not found — check your .env file")
    


    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(question)
    print(response.text)