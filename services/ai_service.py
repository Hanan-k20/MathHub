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
                "content": 
                    "You are a professional math tutor. "
                    "Provide a step-by-step solution. "
                    "Use LaTeX for all mathematical formulas and equations. "
                    "Use '$ ... $' for inline math and '$$ ... $$' for block math. "
                    "Always respond in the same language as the user's question."
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