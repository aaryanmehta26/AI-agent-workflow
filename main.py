import os

# Run "uv sync" to install the below packages
import requests
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def generate_post(topic: str) -> str:
    # call AI (LLM) to generate a post based on the topic

    # prompt engineering: crafting a prompt to get the desired output from the LLM
    prompt = f""" 

 You are an expert social media manager and content creator and you excel at crafting engaging and original social media posts for X (formerly Twitter).

 Your task is to create a compelling and engaging social media post based on the following topic: "{topic}". 
 The post should be concise, attention-grabbing, and tailored for a general audience. 

 Please ensure that the content is original and does not contain any sensitive or inappropriate material.
"""

    payload = {
        "model": "gpt-4.1-nano",
        "input": prompt,
    }

    print("Generating post...")
    response = requests.post("https://api.openai.com/v1/responses",
                             json=payload, headers={
                                 "Content-Type": "application/json",
                                 "Authorization": f"Bearer {OPENAI_API_KEY}"
                             })
    return response.json().get("output", [{}])[0].get("content", [{}])[0].get("text", "")


def main():

    # take user input => call AI (LLM) to generate a post => output the post to the user
    user_input = input("What topic would you like to write about? ")
    post = generate_post(user_input)
    print("Here is your generated post:")
    print(post)


if __name__ == "__main__":
    main()
