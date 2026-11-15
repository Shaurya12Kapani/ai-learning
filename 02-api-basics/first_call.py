import os
import getpass
import anthropic

if not os.environ.get("ANTHROPIC_API_KEY"):
        os.environ["ANTHROPIC_API_KEY"] = input("Paste your key: ").strip()

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=300,
    messages=[{"role": "user", "content": "Explain gear ratio in two sentences."}],
)
print(message.content[0].text)
