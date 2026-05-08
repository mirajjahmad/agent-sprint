import os
from anthropic import Anthropic
from dotenv import load_dotenv

#load the keys from .env
load_dotenv()

#initialize the client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

#send a test message
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "tell me alfred is online"}
    ]
)

print(message.content[0].text)

#git init: initializes a brand new repository, basically creates a hidden tracking system in this folder
#git add .: tells git to take a snapshot of every file in the folder (the dot means everything)
#git commit -m "alfred is online": saves that snapshot with a permanent note so you can always come back to this exact version of your code later