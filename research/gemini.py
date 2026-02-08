
from google import genai
client = genai.Client(api_key="AIzaSyCKBVCABd4csDb3TO1v-MXZlXrTPbW42Ag")




print("Gemini Chatbot (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        break

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=user_input
    )

    print("Bot:", response.text)