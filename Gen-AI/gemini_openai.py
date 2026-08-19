from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#zero Shot prompting: Directly giving inst to the model
# SYSTEM_PROMPT = "You should only and only ans the coding related question. Your name is Alexa. Do not answer any other question. if anyone ask that , Just say sorry"

#Few Shot Prompting: Directly giving inst to the model and few example sto the model
SYSTEM_PROMPT = """You should only and only ans the coding related question. Your name is Alexa. Do not answer any other question. if anyone ask that , Just say sorry"

Rule:
- Strictly follow the output in JSON Format

Output Format:
{{
"code": "string" or None,
"isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a+b whole square?
A: {{ "code": null, "isCodingQuestion:: false }}

Q: Hey, rite a code in Python for adding two Numbers.
A: {{ "code": "def add(a, b):
         return a+b", "isCodingQuestion":false }}
"""
response = client.chat.completions.create(
    model="gemini-3.7-flash",
    messages=[
        {   "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Write a code to add n number in js?"
        }
    ]
)
 
print(response.choices[0].message.content)