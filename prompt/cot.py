from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()
key = os.getenv("GEMINI_API_KEY")

print("Key exists:", key is not None)
print("Key starts with:", key[:8] if key else None)
print("Key length:", len(key) if key else 0)

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    # base_url="https://generativelanguage.googleapis.com/v1beta/"
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
   
)
SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

    Example:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN": "content": "We must perform divide that is 15 / 10  = 1.5" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5" }
    PLAN: { "step": "PLAN": "content": "Now finally lets perform the add 3.5" }
    PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans" }
    OUTPUT: { "step": "OUTPUT": "content": "3.5" }
    

"""

message_history=[
    {"role": "system", "content": SYSTEM_PROMPT}
]
user_query= input("👉🏻")
message_history.append({"role": "user", "content": user_query}, )

while True:
    response= client.chat.completions.create(
    model = "gemini-3.6-flash",
    messages= message_history
    )
    
    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    
    
    parsed_result = json.load(raw_result)
    
    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break
        

# response = client.chat.completions.create(
#     model="gemini-3.6-flash",
#     messages=[
#         { "role": "system", "content": SYSTEM_PROMPT },
#         { "role": "user", "content": "Hey, write a code to add n numbers in js"},
#         {"role": "assistant", "content": json.dumps({"step": "START", "content":"You want javascript code to add 'n' numbers."})},
#         {"role": "assistant", "content": json.dumps({
#   "step": "PLAN",
#   "content": "The user wants a JavaScript function to add 'n' numbers. I should consider methods like using array `reduce` or rest parameters (`...numbers`) which allow taking variable arguments."
# })},
# {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "I will construct a clean JavaScript function using modern ES6 rest parameters (`...numbers`) and the `Array.prototype.reduce()` method to sum up any number of arguments passed to it, along with usage examples."})},
#    {"role": "user", "content": json.dumps({
#   "step": "OUTPUT", "content": "Here is a flexible JavaScript function that can take any number of arguments (`n` numbers) and return their sum using rest parameters (`...numbers`) and the `reduce` method:\n\n```javascript\n// Function to add n numbers\nfunction addNumbers(...numbers) {\n  return numbers.reduce((sum, current) => sum + current, 0);\n}\n\n// Examples:\nconsole.log(addNumbers(5, 10)); // Output: 15\nconsole.log(addNumbers(1, 2, 3, 4, 5)); // Output: 15\nconsole.log(addNumbers(10, -2, 3.5, 100)); // Output: 111.5\n\n// Alternatively, if you have an array of numbers:\nconst numberArray = [10, 20, 30, 40];\nconsole.log(addNumbers(...numberArray)); // Output: 100\n```"
# })},

#     ]
# )

# print(response.choices[0].message.content)
