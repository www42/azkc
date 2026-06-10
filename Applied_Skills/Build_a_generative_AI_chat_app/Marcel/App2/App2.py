import os
import sys
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import ChatCompletionsClient

load_dotenv()
endpoint = os.getenv("endpoint")
deployment_name = os.getenv("deployment_name")
api_key = os.getenv("api_key")

if not all([endpoint, deployment_name, api_key]):
    sys. exit("Missing env vars: ensure endpoint, deployment_name, and api_key are set.")

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key),
    max_tokens=800
)

chat_history = []
# TODO: Limit the conversation history
MAX_TURNS = 10

def set_system_message(content: str):
    """Set the system message at the start of the chat."""
    system_message = {"role": "system", "content": content}
    chat_history.insert(0, system_message)

def update_chat_history(message: str, role: str):
    """Add a message to the chat history."""
    chat_history.append({"role": role, "content": message})

def trim_chat_history():
    """Trim chat history to keep system message + last 10 turns (20 messages)."""
    if not chat_history or chat_history[0]["role"] != "system":
        return
    system_message = chat_history[0]
    conversation_messages = chat_history[1:]
    if len(conversation_messages) > MAX_TURNS * 2:
        conversation_messages = conversation_messages[-MAX_TURNS * 2:]
    chat_history[:] = [system_message] + conversation_messages

def send_message(user_input: str):
    """Send user input to the model and print the full response."""
    # TODO: Task 3 - Add conversation history (part 1)
    update_chat_history(user_input,"user") 

    # TODO: Task 3 - Trim chat history
    trim_chat_history()

    response = client.complete(
        model=deployment_name,
        messages=chat_history
    )
    assistant_reply = response.choices[0].message.content
    print("\nAssistant:", assistant_reply)
    # TODO: Task 3 - Add conversation history (part 2)
    update_chat_history(assistant_reply,"assistant")  

set_system_message("You are a helpful, concise assistant.")
print ("Type 'exit' or 'quit' to end the conversation.\n")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print ("Goodbye!")
        break
    if not user_input:
        continue
    send_message(user_input)