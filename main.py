import os
from groq import Groq

userapiinput = input("API key: ")
client = Groq(api_key=userapiinput)
usermodelinput = input("Model: ")

messages = [
        {"role": "system", "content": "You are Groqium. An helpful AI assistant that shall and must help the user with whatever the user requests. You are powered by the users Groq AI API key hosted by the Groq company, be warned that you (Groqium) are not at all related to the Groq Company or any of its workers. Your code was made by johnblackwood1 on github.com. Thank you."}
]

print("Welcome to Groqium!")

running = True
while running:
    userinput = input("<You>: ")
    if userinput == "/goodbye":
        print("Goodbye!")
        running = False
    messages.append({"role": "user", "content": userinput})

    completion = client.chat.completions.create(
            model=usermodelinput,
            messages=messages,
            temperature=0.7,
            max_tokens=500,
    )
    responce = completion.choices[0].message.content
    print(f"<Bot>: {responce}")

    messages.append({"role": "assistant", "content": responce})
