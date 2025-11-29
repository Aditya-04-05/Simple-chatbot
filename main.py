import os
import cohere
from dotenv import load_dotenv
load_dotenv()

def main():
  api_key = os.getenv("COHERE_API_KEY")
  if not api_key:
    raise RuntimeError("Please set COHERE_API_KEY in Replit Secrets.")

  client = cohere.ClientV2(api_key)

  print("🤖 Cohere Chatbot — type 'exit' to quit.\n")

  system_prompt = "You are a friendly assistant. Keep answers short and simple and in a human tone."
  while True:
    user_inp = input("You: ")

    if user_inp.lower() == "exit":
      print("Bot: Goodbye!")
      break

    response = client.chat(
        model="command-a-03-2025",
        messages=[{
            "role": "system",
            "content": system_prompt
        }, {
            "role": "user",
            "content": user_inp
        }],
        max_tokens=150
    )

    # Extract text
    try:
      answer = response.message.content[0].text
    except:
      answer = "(No response)"

    print("Bot:", answer, "\n")


if __name__ == "__main__":
  main()
