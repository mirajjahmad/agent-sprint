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