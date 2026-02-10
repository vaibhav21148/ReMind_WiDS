import google.generativeai as genai
import json
import os
import time
from datetime import datetime

REAL_API_KEY = "AIzaSyC_qmEWq29rGiUrTipPaUkV3ZyRlnFR3-M" 

DATA_FILE = "flashcards.json"
genai.configure(api_key=REAL_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_card_with_ai(data):
    question = input("\nAsk a question to learn: ")
    
    print("Asking Gemini for the answer...")
    try:
        # AI generates the answer strictly
        response = model.generate_content(f"Answer this question briefly and clearly for a flashcard: {question}")
        answer = response.text
        print(f"AI Suggested Answer: {answer}")
        
        # Save it
        new_card = {
            "question": question,
            "answer": answer,
            "level": 0, # Level 0 means new
            "last_reviewed": datetime.now().isoformat()
        }
        data.append(new_card)
        save_data(data)
        print("Saved to deck!")
        
    except Exception as e:
        print(f"Error connecting to AI: {e}")

def review_cards(data):
    print("\n--- Review Session ---")
    current_time = datetime.now()
    count = 0
    
    # Simple Logic: Level 0 = 0 mins, Level 1 = 1 min, Level 2 = 5 mins
    intervals = {0: 0, 1: 1, 2: 5, 3: 10} 
    
    for card in data:
        last_time = datetime.fromisoformat(card["last_reviewed"])
        required_wait = intervals.get(card["level"], 60) # default 60 mins for high levels
        
        # Check time difference in minutes
        diff = (current_time - last_time).total_seconds() / 60
        
        if diff >= required_wait:
            print(f"\nQ: {card['question']}")
            input("Press Enter to reveal answer...")
            print(f"A: {card['answer']}")
            
            check = input("Did you recall it? (y/n): ")
            if check.lower() == 'y':
                card["level"] += 1
                print("Level Up!")
            else:
                card["level"] = 1
                print("Resetting level.")
            
            card["last_reviewed"] = current_time.isoformat()
            save_data(data)
            count += 1
            
    if count == 0:
        print("Nothing to review right now.")

def main():
    data = load_data()
    while True:
        print("\n1. Ask Bot (Create Card)")
        print("2. Review Cards")
        print("3. Quit")
        choice = input("Choice: ")
        
        if choice == '1':
            add_card_with_ai(data)
        elif choice == '2':
            review_cards(data)
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
