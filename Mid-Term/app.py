import os
from google import genai

# Best practice: Set your API key as an environment variable (GEMINI_API_KEY)
# Alternatively, pass it directly: client = genai.Client(api_key="YOUR_KEY")
client = genai.Client(api_key="Gemini_API_Key")

def get_ai_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
    )
    return response.text

def main():
    print("--- Simple Gemini Clone ---")
    print("Type 'exit' to stop the session.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        print(f"AI: {get_ai_response(user_input)}")

if __name__ == "__main__":
    main()