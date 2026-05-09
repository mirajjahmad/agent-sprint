#dictionary will store paper title, pmid, whether it's legit (peer-reviewed, strong evidence, no funding bias), etc.
paper = {
    "title": "Effect of Redensyl on Hair Growth",
    "pmid": 32473084,
    "is_legit": True,
    "source": {
        "journal": "Dermatol Ther",
        "year": 2020
    }
}

print(f"journal:{paper['source']['journal']}")

papers = [
    {"title": "Redensyl Study", "is_legit": True},
    {"title": "Snake Oil Study", "is_legit": False}
]

print(f"first paper: {papers[0]}")

import json

#turn list of papers into a json string
papers_json = json.dumps(papers, indent=4)

print("json format:")
print(papers_json)

import pandas as pd

#turns list of papers into dataframe
df = pd.DataFrame(papers)
print("\ndataframe format:")
print(df)

#print only if legit
print("\nfiltering for legit research:")
print(df[df['is_legit'] == True])