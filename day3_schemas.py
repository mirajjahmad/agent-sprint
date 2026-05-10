from pydantic import BaseModel
from typing import List, Optional

class Source(BaseModel):
    journal: str
    year: int

class ResearchPaper(BaseModel):
    title: str
    pmid: int
    source: Source
    tags: List[str] = [] #if no tags, run anyways and leave field empty
    summary: Optional[str] = None #if no summary, run anyways and leave field empty

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