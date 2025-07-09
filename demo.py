# print("demo works!")
# just use this to play around 


# test API keys
from dotenv import load_dotenv
import os


load_dotenv(override = True)
api_key = os.getenv("ANTHROPIC_API_KEY")

print(api_key)
