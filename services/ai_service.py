import os
from openai import OpenAI
from dotenv import load_dotenv  

load_dotenv()

# Initialize the client
client = OpenAI()

def solve_math(question):
    response = client.chat.completions.create(
        model="gpt-5-mini", 
        messages=[
            {
                "role": "system", 
                "content": (
                    r"You are a professional math tutor and LaTeX expert. "
                    r"1. LANGUAGE: Respond in the EXACT SAME language as the user. If Arabic, stay in Arabic. "
                    r"2. RECOGNITION: Identify any math symbols, verbal descriptions (e.g., 'square root of x'), or messy notations and convert them into formal math. "
                    r"3. LATEX ONLY: Never use plain text for math. Use LaTeX for every single number, variable, and symbol. "
                    r"4. FORMATTING: Wrap ALL math in \( ... \) for inline and \[ ... \] for blocks. "
                    r"5. CONVERSION: If the user uses Arabic variables (like 'س' or 'ص'), convert them to standard Latin variables (x, y) in LaTeX. "
                    r"Example: If user says '2س + 5', output '\( 2x + 5 \)'. "
                )
            },
            {
                "role": "user", 
                "content": question
            }
        ],
       # temperature=0 
    )
    return response.choices[0].message.content
    # This returns the full explanation, pulling from your $5.00 credit
    return response.choices[0].message.content


# Try
if __name__ == "__main__":
    test_question = "Solve 2x + 10 = 20" 
    result = solve_math(test_question)
    print("--- AI RESPONSE START ---")
    print(result.encode('utf-8', errors='replace').decode('utf-8'))
    print("--- AI RESPONSE END ---")