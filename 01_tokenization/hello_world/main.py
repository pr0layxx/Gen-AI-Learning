from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages =[
        
        {"role": "user",
         "content": "Hey , do you know what is gen ai?"}
    ]
)

print(response.choices[0].message.content)