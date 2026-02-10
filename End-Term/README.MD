# End-Term Submission (Gemini Edition)

This project contains 3 chatbots built using Python and Google's Gemini API.

## Setup Instructions
1. **Install Python Libraries:**
   You need the Google AI library. Run this in your terminal:
   `pip install google-generativeai`

2. **API Key:**
   Open each python file (`socratic_bot.py`, etc.) and paste your API key where it looks like this:
   `genai.configure(api_key="AIzaSy...")`

## Problem 1: Socratic Tutor
* **File:** `/Problem_1/socratic_bot.py`
* **Description:** This bot remembers what you said (history saved in `history.json`). It follows the "Socratic method"—it never answers directly, only asks questions.
* **How to run:** `python socratic_bot.py`

## Problem 2: Spaced Repetition Bot
* **File:** `/Problem_2/spaced_rep_bot.py`
* **Description:**
    1. You ask a question.
    2. Gemini generates the answer and saves it as a flashcard.
    3. The bot tracks when you need to review it based on how well you remember it (Levels 0, 1, 2, 3).
* **How to run:** `python spaced_rep_bot.py`

## Problem 3: Mood Diary Bot (My Idea)
* **File:** `/Problem_3/diary_bot.py`
* **Description:** A personal journal where Gemini acts as a therapist/friend. It reads your entry, detects your mood, and saves an encouraging comment alongside your text.
* **How to run:** `python diary_bot.py`