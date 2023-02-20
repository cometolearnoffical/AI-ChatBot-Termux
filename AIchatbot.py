import openai
import os
from tkinter import *

# Set up the OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Set up the UI
root = Tk()
root.title("AI Chatbot")

# Add a text box for the chat history
chat_history = Text(root, height=20, width=50)
chat_history.pack()

# Add a text box for user input
user_input = Entry(root, width=50)
user_input.pack()

# Define a function to handle user input and generate a response from OpenAI
def generate_response():
    # Get the user input
    input_text = user_input.get()

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=input_text,
        temperature=0.5,
        max_tokens=50,
        n=1,
        stop=None,
        timeout=10,
    )

    # Extract the generated text from the API response
    output_text = response.choices[0].text.strip()

    # Display the response in the chat history
    chat_history.insert(END, "You: " + input_text + "\n")
    chat_history.insert(END, "AI: " + output_text + "\n")

    # Clear the user input box
    user_input.delete(0, END)

    # Run Termux command if "termux" or "android" is present in the user input
    if "termux" in input_text.lower() or "android" in input_text.lower():
        os.system("termux-open-url https://play.google.com/store/apps/details?id=com.termux")

    # Run Kali Linux command if "kali" or "linux" is present in the user input
    if "kali" in input_text.lower() or "linux" in input_text.lower():
        os.system("kali-linux-command-here")

# Add a button to submit user input
submit_button = Button(root, text="Send", command=generate_response)
submit_button.pack()

# Start the UI main loop
root.mainloop()
