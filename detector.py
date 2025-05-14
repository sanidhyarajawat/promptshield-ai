import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_prompt_security(system_prompt, messages):
    chat_input = [
        {"role": "system", "content": open("prompts/analysis_prompt.txt").read()},
        {"role": "user", "content": f"System Prompt:\n{system_prompt}\n\nChat History:\n{json.dumps(messages, indent=2)}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_input,
        temperature=0.0
    )

    try:
        return json.loads(response.choices[0].message.content.strip())
    except Exception as e:
        return {"error": str(e)}