from pydantic import BaseModel
from typing import List, Optional

class Source(BaseModel):
    journal: str
    year: int

class ResearchPaper(BaseModel):
    title: str
    pmid: int
    source: Source
    tags: List[str] = []
    summary: Optional[str] = None

#test data
data = {
    "title": "Bio-Inspired Design",
    "pmid": 87654321,
    "source": {
        "journal": "Nature",
        "year": 2025
    },
    "tags": ["biology", "innovation"],
    "summary": "a very cool paper about nature"
}

paper = ResearchPaper(**data)
print(f"source: {paper.source.journal}")
print(f"summary: {paper.summary}")