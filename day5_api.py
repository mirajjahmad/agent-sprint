import os
import json
from anthropic import Anthropic
from dotenv import load_dotenv
from models import ResearchPaper, Source

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

#example abstract from pubmed
abstract = """
Redensyl is a novel hair growth active compound targeting hair follicle stem cells.
In a clinical study of 26 volunteers over 84 days, Redensyl showed a 17% increase in 
hair growth versus placebo. The compound activates DHQG and EGCG2 to stimulate 
dermal papilla cell division. Published in the Journal of Cosmetic Dermatology, 2014.
"""

prompt = f"""
you are a biotech research assistant. extract the key info from this abstract and return ONLY a valid JSON object with these exact fields:
- title (str)
- pmid (int, make up a plausible one if not available)
- source: {{ journal (str), year (int) }}
- tags (list of strings)
- summary (str, one sentence)

abstract:
{abstract}

return ONLY the json, no extra text.
"""

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt}]
)

#parse the json and validate with pydantic
#strip the backticks that alfred added
clean_text = response.content[0].text.replace("```json", "").replace("```", "").strip()
raw = json.loads(clean_text)
paper = ResearchPaper(**raw)

print(f"title: {paper.title}")
print(f"summary: {paper.summary}")
print(f"tags: {paper.tags}")
print(f"journal: {paper.source.journal}")
print(f"year: {paper.source.year}")
print(f"pmid: {paper.pmid}")