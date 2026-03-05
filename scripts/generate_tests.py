import os
from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ["NVIDIA_API_KEY"]
)

# Read source code
with open("src/calculator.js") as f:
    code = f.read()

prompt = f"""
You are a senior QA engineer.

Generate Jest unit tests for the following JavaScript code.

Code:
{code}

Requirements:
- valid Jest syntax
- edge cases
- invalid inputs
- division by zero case
- multiple scenarios

Return ONLY the test code.
"""

completion = client.chat.completions.create(
    model="minimaxai/minimax-m2.5",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.3,
    max_tokens=2000
)

tests = completion.choices[0].message.content

# Save generated tests
with open("tests/generated.test.js", "w") as f:
    f.write(tests)

print("AI tests generated successfully")