#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import json
#from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class ChatGPT:
    def __init__(self):
        # Load environment variables
        self.api_key = os.getenv("API_KEY")
        self.client = OpenAI(api_key=self.api_key)

    def summarize_and_breakdown(self, text):
        try:
            # Sending request to OpenAI
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Return a response in JSON format with two fields: 'summary' containing a summary of the task in no more than 8 words, and 'breakdown' listing the simpler tasks."},
                    {"role": "user", "content": text}
                ]
            )

            # Extracting the response and converting it to a Python dictionary
            response_content = response.choices[0].message.content
            structured_response = json.loads(response_content)

            return structured_response
        except Exception as e:
            return f"An error occurred: {e}"

# if __name__ == "__main__":
#     chat_gpt = ChatGPT()
#     result = chat_gpt.summarize_and_breakdown("Create readme of a arduino turn led on project")
#     print(result)