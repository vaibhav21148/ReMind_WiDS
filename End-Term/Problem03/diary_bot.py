import google.generativeai as genai
import json
import os
from datetime import datetime

REAL_API_KEY = "AIz" 
   
JOURNAL_FILE = "my_journal.json"
genai.configure(api_key=REAL_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def load_journal():
    print("loading..\n")
    if not os.path.exists(JOURNAL_FILE):
        print("going in if\n")
        return []
    with open(JOURNAL_FILE, "r") as f:
        print("file exist")
        return json.load(f)

def save_journal(data):
    with open(JOURNAL_FILE, "w") as f:
        json.dump(data, f, indent=4)

def write_entry(journal):
    print("\nDear Diary... (type your thoughts)")
    text = input("> ")
    
    # AI Feature: Analyze mood
    prompt = f"Read this diary entry: '{text}'. 1. Identify the mood (one word). 2. Write a one-sentence encouraging response."
    
    try:
        response = model.generate_content(prompt)
        ai_reply = response.text
        print(f"\nAI Analysis:\n{ai_reply}")
        
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "text": text,
            "ai_analysis": ai_reply
        }
        journal.append(entry)
        save_journal(journal)
        
    except Exception as e:
        print("AI offline, saving text only.")
        journal.append({"date": datetime.now().strftime("%Y-%m-%d %H:%M"), "text": text, "ai_analysis": "None"})
        save_journal(journal)

def read_entries(journal):
    print("\n--- Past Entries ---")
    for item in journal:
        print(f"[{item['date']}]")
        print(f"Entry: {item['text']}")
        print(f"AI: {item['ai_analysis']}")
        print("-" * 30)

def main():
    journal = load_journal()
    while True:
        print("\n1. New Entry")
        print("2. Read Diary")
        print("3. Quit")
        choice = input("Choice: ")
        
        if choice == '1':
            write_entry(journal)
        elif choice == '2':
            read_entries(journal)
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
