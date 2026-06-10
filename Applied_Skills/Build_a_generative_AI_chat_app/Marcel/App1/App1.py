import os
import sys
from dotenv import load_dotenv
# TODO: Reference Azure AI Foundry SDK
from openai import OpenAI

load_dotenv()
endpoint = os.getenv("endpoint")
deployment_name = os.getenv("deployment_name")
api_key = os.getenv("api_key")
api_version = "2024-12-01-preview"

if not all([endpoint, deployment_name, api_key]):
    sys.exit ("Missing env vars: ensure endpoint, deployment_name, and api_key are set.")

# TODO: Initialize the client
client = OpenAI(
    base_url = endpoint,
    api_key = api_key
)

question = input ("Ask the AI a question: ").strip()
if not question:
    sys.exit ("No question provided.")

messages = [
    {"role": "system", "content": "You are a helpful assistant. Return response in markdown only." },
    {"role": "user", "content": question }  
]

# TODO: Submit the message to Azure AI Foundry
response = client.chat.completions.create(
    model = deployment_name,
    messages = messages
)

# TODO: Output the message in the console
completion = response.choices[0].message.content

print("\nassistant:",completion)
print()