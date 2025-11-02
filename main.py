import tiktoken
from openai import OpenAI
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(model="gpt-4o-mini",

messages=[{"role":"user","content": "Hey there"

}]
)

print(response.choices[0].message.content)


# Get the encoding for OpenAI models
enc = tiktoken.encoding_for_model("gpt-4")
print(enc)

text = " Hi , i am Ajit"

tokens = enc.encode(text)

print("Tokens" , tokens)
