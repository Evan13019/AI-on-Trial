import os
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd
from tqdm import tqdm

# Load .env variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=api_key)

# Choose model: Gemini 1.5 is most powerful (context up to 1M tokens)
model = genai.GenerativeModel("gemini-1.5-pro")

# Example prompts
prompts = [
    "Summarize the Miranda v. Arizona case in two sentences.",
    "List 3 potential legal biases that might appear in jury selection.",
    "Write a counterargument to this ruling: [Insert ruling text here]."
]

results = []

# Run each prompt through Gemini
for prompt in tqdm(prompts):
    response = model.generate_content(prompt)
    results.append({
        "prompt": prompt,
        "response": response.text.strip()
    })

# Save results to CSV
df = pd.DataFrame(results)
df.to_csv("gemini_experiment_results.csv", index=False)
print("Saved results to gemini_experiment_results.csv")