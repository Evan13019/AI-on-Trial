from dotenv import load_dotenv
import os
from openai import OpenAI




from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

#if not api_key:
#    raise ValueError("API key not loaded from .env")

client = Anthropic(api_key="enter key here, couldnt get env working will fix later")

response = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=100,
    temperature=0.5,
    messages=[{"role": "user", "content": "hello claude"}]
)

print(response.content[0].text)


'''
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a short poem about LLMs."}
    ]
)

print(response.choices[0].message.content)
'''


