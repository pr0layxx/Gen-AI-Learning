from openai import OpenAI

client = OpenAI(
    api_key="AQ.Ab8RN6JBoYvqJHwUluJTCKNhaSWewBFGBcGxazJtaWjdineYkw",
    base_url="https://generativelanguage.googleapis.com/v1beta/",
)

# ZERO PROMPTING 
# SYSTEM_PROMPT = "You should only and only ans the coding related questions. Do not ans anything else. Your name is Alexa. If user asks something other than coding, just say sorry."
#FEW - ADDING SOME EXAMPLES 

# FEW STRUCTURED PROMPTING
SYSTEM_PROMPT = """
You should only and only ans the coding related questions. Do not ans anything else. Your name is Alexa. If user asks something other than coding, just say sorry.

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
 "code": "string" or null,
 "isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a + b whole square?
A: {{ "code": null, "isCodingQuestion": false }}

Q: Hey, Write a code in python for adding two numbers.
A: {{ "code": "def add(a, b):
        return a + b", "isCodingQuestion": false }}
"""


response = client.chat.completions.create(
    model="gemini-3.7-flash",
    messages =[
        {"role": "system", "content": SYSTEM_PROMPT },
        {"role": "user",
         "content": "Hey ,Hey, write a code to add n numbers in js"}
    ]
)

print(response.choices[0].message.content)