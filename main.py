import openai
import config


openai.api_key = config.api_key

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                             messages=[{"role":"user","content": "Whats is the OpenAI mission"}])

#print(response)
print(response.choices[0].message.content)

