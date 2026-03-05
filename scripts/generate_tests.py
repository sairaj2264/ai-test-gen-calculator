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

Rules:
- Output ONLY valid JavaScript
- Do NOT include explanations
- Do NOT include <think> tags
- Do NOT include markdown
- Only return Jest test code

Example format:

const calc = require("../src/calculator");

test("adds numbers", () => {{
  expect(calc.add(2,3)).toBe(5);
}});
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

# Remove reasoning tags
tests = tests.replace("<think>", "").replace("</think>", "")

# Remove markdown code blocks
tests = tests.replace("```javascript", "").replace("```", "")

# Trim whitespace
tests = tests.strip()

# Save generated tests
with open("tests/generated.test.js", "w") as f:
    f.write(tests)

print("AI tests generated successfully")
print("===== GENERATED TESTS =====")
print(tests)
print("===========================")