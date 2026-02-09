import os
import random
from google import genai

client = genai.Client(api_key="Gemini_API_Key")
history = []
counter = 0

def get_ai_response(prompt):
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return response.text

def generate_quiz(topic):
    prompt = f"The user just learned about '{topic}'. Generate a challenging one-sentence quiz question to test their recall on this topic."
    return get_ai_response(prompt)

def main():
    global counter, history
    print("--- ReMind: Counter Bot (Quiz every 5 queries) ---")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit": break

        # Track interaction
        history.append(user_input)
        counter += 1

        if counter >= 5:
            # Trigger Quiz
            quiz_topic = random.choice(history)
            print("\n[!] COUNTER REACHED 5. TIME FOR A RECALL QUIZ.")
            print(f"AI Quiz: {generate_quiz(quiz_topic)}")
            
            user_answer = input("Your Answer: ")
            print("AI: Verification complete. Resetting counter...")
            
            # Reset
            counter = 0
            history = []
        else:
            print(f"AI: {get_ai_response(user_input)}")
            print(f"(Progress to quiz: {counter}/5)")

if __name__ == "__main__":
    main()