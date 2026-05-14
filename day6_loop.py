import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

abstract = "Redensyl targets hair follicle stem cells to increase hair growth by 17%."
target_length = 2  #we want exactly two sentences

def run_agent_loop():
    current_summary = ""
    for i in range(1, 4):  #give him 3 tries to get it right
        print(f"\n--- attempt {i} ---")
        
        prompt = f"summarize this in exactly {target_length} sentences: {abstract}"
        if current_summary:
            prompt += f"\nyour last attempt was: {current_summary}. it was wrong. try again."

        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=100,
            messages=[{"role": "user", "content": prompt}]
        )
        
        current_summary = response.content[0].text
        print(f"alfred says: {current_summary}")

#the "observation" step
        sentence_count = current_summary.count('.')
        if sentence_count == target_length:
            print("goal reached. loop stopping.")
            break
        else:
            print(f"failed. only found {sentence_count} sentences. retrying...")

run_agent_loop()