import os
import json
import anthropic

if not os.environ.get("ANTHROPIC_API_KEY"):
    os.environ["ANTHROPIC_API_KEY"] = input("Paste your key: ").strip()

client = anthropic.Anthropic()

system = (
    "You are a mechanical engineering assistant. Reply with only a JSON object, "
    "no extra text, with these keys: gear_ratio (number), output_rpm (number), "
    "output_torque_nm (number), explanation (string, one sentence). Assume ideal gearing."
)

question = "A 20-tooth gear drives a 60-tooth gear at 3000 rpm with 10 N.m input torque."

message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=300,
    system=system,
    messages=[{"role": "user", "content": question}],
)

text = "".join(b.text for b in message.content if b.type == "text").strip()
text = text.replace("```json", "").replace("```", "").strip()

try:
    data = json.loads(text)
except json.JSONDecodeError:
    print("Not valid JSON:", text)
    raise SystemExit

print(data)
print("Output speed:", data["output_rpm"], "rpm")
