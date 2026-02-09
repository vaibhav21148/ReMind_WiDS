import os
import time
from datetime import datetime, timedelta
from google import genai

client = genai.Client(api_key="Gemini_API_Key")
# Stores list of [timestamp, query_text, has_been_quizzed]
memory_vault = []

def get_ai_response(prompt):
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return response.text

def main():
    print("--- ReMind: Time Bot (Recall after 10 mins) ---")
    
    while True:
        current_time = datetime.now()

        # Check for pending quizzes
        for entry in memory_vault:
            # If 10 mins passed and we haven't quizzed yet
            if not entry[2] and current_time >= entry[0] + timedelta(minutes=10):
                print(f"\n\n[!] 10-MINUTE MEMORY CHECK")
                quiz_q = get_ai_response(f"Ask a question to see if I remember the topic: {entry[1]}")
                print(f"AI: {quiz_q}")
                entry[2] = True # Mark as quizzed
                input("\n(Press Enter to continue)")

        # Normal Chat
        user_input = input("\nYou (or wait for quiz): ")
        if user_input.lower() == "exit": break
        
        # Save to memory with timestamp
        memory_vault.append([datetime.now(), user_input, False])
        
        print(f"AI: {get_ai_response(user_input)}")
        print(f"Logged at: {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()