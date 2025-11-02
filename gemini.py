from google import genai

client = genai.Client(api_key="AIzaSyADRmDBVM27GBAvEBS0UG7fUdIQb_sHuF4")

response = client.models.generate_content(model="gemini-2.5-flash",

contents="Hey there Gemini"


)

print(response.text)