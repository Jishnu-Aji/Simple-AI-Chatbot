import streamlit as st
import random

# Chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey"]
    jokes = [
        "Why did the computer catch a cold? Because it forgot to close its Windows!",
        "Why do programmers prefer dark mode? Because light attracts bugs 😄",
        "Why was the JavaScript developer sad? Because he didn’t know how to ‘null’ his feelings."
    ]

    if any(greet in user_input for greet in greetings):
        return "Hello! 😊 How can I help you today?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😄"

    elif "your name" in user_input:
        return "I'm a simple AI chatbot built with Python 🤖"

    elif "joke" in user_input:
        return random.choice(jokes)

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! 👋 Have a great day!"

    else:
        return "Hmm 🤔 I’m still learning. Can you ask something else?"

# Streamlit UI
st.set_page_config(page_title="Simple AI Chatbot", page_icon="🤖")
st.title("🤖 Simple AI Chatbot")

st.write("Type a message and press Enter to chat with the bot.")

user_input = st.text_input("You:", "")

if user_input:
    response = chatbot_response(user_input)
    st.text_area("Chatbot:", value=response, height=100, disabled=True)
