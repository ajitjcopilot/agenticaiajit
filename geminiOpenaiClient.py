import tiktoken
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key="AIzaSyADRmDBVM27GBAvEBS0UG7fUdIQb_sHuF4", base_url="https://generativelanguage.googleapis.com/v1beta/")

response = client.chat.completions.create(model="gemini-2.5-flash",

messages=[{"role":"user","content": "explain GPT"

}]
)

print(response.choices[0].message.content)


# Get the encoding for OpenAI models
enc = tiktoken.encoding_for_model("gpt-4")
print(enc)

text = " Hi , i am Ajit"

tokens = enc.encode(text)

print("Tokens" , tokens)
