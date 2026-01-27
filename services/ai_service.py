import os
from openai import OpenAI
from dotenv import load_dotenv  

load_dotenv()

# Initialize the client
client = OpenAI()

def solve_math(question):
    # We changed the system prompt to match the user's language
    response = client.chat.completions.create(
        model="gpt-5-mini", # The fast and cheap model from your list
        messages=[
            {
                "role": "system", 
               "content": (
                    r"You are a professional math tutor. "
                    r"1. LANGUAGE: You MUST respond in the EXACT SAME language as the user's question. If they ask in Arabic, answer in Arabic. "
                    r"2. MATH FORMATTING: Never use plain text or unicode characters for math (like 2⁢𝑥 or 1/2). "
                    r"3. LATEX ONLY: Use LaTeX for every single number, variable, and equation. "
                    r"4. DELIMITERS: Wrap ALL math in \( ... \) for inline and \[ ... \] for blocks. "
                    r"Example: Instead of '2x=1', write '\( 2x = 1 \)'. Instead of '1/2', write '\( \frac{1}{2} \)'. "
                )
            },
            {
                "role": "user", 
                "content": question
            }
        ],
        # temperature=0
    )
    
    # This returns the full explanation, pulling from your $5.00 credit
    return response.choices[0].message.content


# Try
if __name__ == "__main__":
    test_question = "Solve 2x + 10 = 20" 
    result = solve_math(test_question)
    print("--- AI RESPONSE START ---")
    print(result.encode('utf-8', errors='replace').decode('utf-8'))
    print("--- AI RESPONSE END ---")