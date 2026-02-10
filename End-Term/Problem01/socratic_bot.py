import google.generativeai as genai
import json
import os

# SETUP: Put your Gemini API Key here

REAL_API_KEY = "AIzaSyC_qmEWq29rGiUrTipPaUkV3ZyRlnFR3-M" 

try:
    genai.configure(api_key=REAL_API_KEY)
except Exception as e:
    print(f"Configuration Error: {e}")

HISTORY_FILE = "history.json"

# We use a "system instruction" to force the Socratic behavior
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="You are a Socratic tutor. You must NEVER answer a question directly. Instead, guide the user to the answer by asking probing questions. Keep your responses short."
)

def load_history():
    # If file doesn't exist, start fresh
    if not os.path.exists(HISTORY_FILE):
        return []
    
    # If file exists, try to read it. If it's empty/broken, start fresh.
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def main():
    print("--- Socratic Bot (Gemini Powered) Started ---")
    print("Type 'quit' to exit.\n")
    
    # 1. Load the raw JSON list (now crash-proof)
    history_data = load_history()
    
    # 2. Convert our JSON list to Gemini's format 
    # (Gemini uses 'model' instead of 'assistant')
    gemini_history = []
    for turn in history_data:
        role = "user" if turn["role"] == "user" else "model"
        gemini_history.append({"role": role, "parts": [turn["content"]]})

    # 3. Start the chat with this history
    chat = model.start_chat(history=gemini_history)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
            
        try:
            # Send message to Gemini
            response = chat.send_message(user_input)
            print(f"Bot: {response.text}")
            
            # Save to our local JSON file manually
            history_data.append({"role": "user", "content": user_input})
            history_data.append({"role": "assistant", "content": response.text})
            save_history(history_data)
            
        except Exception as e:
            print(f"\nError: {e}")
            print("Check if your API Key is correct!")

if __name__ == "__main__":
    main()
