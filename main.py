import os
import json

# Run "uv sync" to install the below packages

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def generate_post(topic: str) -> str:
    with open("post-examples.json", "r") as f:
        examples = json.load(f)

    examples_str = ""
    for i, example in enumerate(examples, 1):
        examples_str += f"""
        <example-{i}>
            <topic>
            {example['topic']}
            </topic>

            <generated-post>
            {example['post']}
            </generated-post>
        </example-{i}>
        """

    prompt = f"""
        You are an expert social media manager, and you excel at crafting viral and highly engaging posts for X (formerly Twitter).

        Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user.
        Avoid using hashtags and lots of emojis (a few emojis are okay, but not too many).

        Keep the post short and focused, structure it in a clean, readable way, using line breaks and empty lines to enhance readability.

        Here's the topic provided by the user for which you need to generate a post:
        <topic>
        {topic}
        </topic>

        Here are some examples of topics and generated posts:
        <examples>
            {examples_str}
        </examples>

        Please use the tone, language, structure , and style of the examples provided above to generate a post that is engaging and relevant to the topic provided by the user.
        Don't use the content from the examples!
"""
    response = client.responses.create(model="gpt-4.1-nano", input=prompt)

    return response.output_text


def main():

    # take user input => call AI (LLM) to generate a post => output the post to the user
    user_input = input("What topic would you like to write about? ")
    post = generate_post(user_input)
    print("Here is your generated post:")
    print(post)


if __name__ == "__main__":
    main()
