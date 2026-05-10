from models import ResearchPaper, Source

data = {
    "title": "Refactored Success",
    "pmid": 99999,
    "source": {"journal": "Clean Code", "year": 2026}
}

paper = ResearchPaper(**data)
print (f"imported successsfully: {paper.title} from {paper.source.journal}")