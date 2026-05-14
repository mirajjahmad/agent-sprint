import os
import json
import pandas as pd
from anthropic import Anthropic
from dotenv import load_dotenv
from models import ResearchPaper, Source

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

#simulated search results for now
abstracts = [
    "Redensyl targets hair follicle stem cells to increase growth by 17%. J. Cosmet. Dermatol 2014. PMID 24852614",
    "Minoxidil 5% foam remains the gold standard for AGA treatment with high clinical efficacy. PMID 12345678."
]

def analyze_papers(abstract_list):
    valid_papers = []
    
    for text in abstract_list:
        print(f"analyzing abstract...")
        
        prompt = f"""
        extract the following research abstract into a JSON object. 
        use this exact structure:
        {{
          "title": "string",
          "pmid": 123,
          "source": {{
            "journal": "string",
            "year": 2024
          }},
          "tags": ["list", "of", "strings"],
          "summary": "one sentence summary"
        }}

        abstract: {text}
        return ONLY raw JSON.
        """
        
        res = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        
        #clean, parse, and validate
        clean_text = res.content[0].text.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_text)

        #validate and create paper object
        paper = ResearchPaper(**data)
        valid_papers.append(paper)
        
    return valid_papers

print("sprint prototype v1 starting...")
results = analyze_papers(abstracts)

#turn our validated objects into a clean table
df = pd.DataFrame([p.model_dump() for p in results])

print("\n--- research brief ---")
print(df[['title', 'pmid', 'summary']])