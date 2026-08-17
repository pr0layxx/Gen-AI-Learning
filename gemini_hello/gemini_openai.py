from openai import OpenAI

client = OpenAI(
    api_key="API-KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/",
)

response = client.chat.completions.create(
    model="gemini-3.7-flash",
    messages =[
        
        {"role": "user",
         "content": "Hey , who are you?"}
    ]
)

print(response.choices[0].message.content)