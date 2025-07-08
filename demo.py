# print("demo works!")
# just use this to play around 

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

print(api_key)