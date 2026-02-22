import streamlit as st
from textblob import TextBlob
import random

st.set_page_config(page_title="Student Mental Health Companion", page_icon="💙", layout="centered")

responses = {
    "negative": [
        "I hear you. It sounds like you're carrying a lot right now. Remember that it's okay to feel this way.",
        "That sounds really tough. Please know that your feelings are valid, and you don't have to go through it alone.",
        "I'm sorry you're feeling this way. Being a student is incredibly stressful. Take a deep breath—you are doing your best."
    ],
    "neutral": [
        "Thank you for sharing that with me. How are you feeling about it?",
        "I'm here listening. Tell me more about how your day has been.",
        "Got it. Is there anything specific on your mind that you'd like to talk about?"
    ],
    "positive": [
        "That's wonderful to hear! It's important to celebrate these good moments.",
        "I'm so glad things are going well for you right now! Keep up that great energy.",
        "That sounds amazing! Cherish this positive feeling."
    ]
}

relaxation_tips = [
    "💡 **Quick Tip:** Try the 4-7-8 breathing method. Inhale for 4 seconds, hold for 7, and exhale for 8.",
    "💡 **Quick Tip:** Take a 5-minute screen break. Look at something 20 feet away to rest your eyes and mind.",
    "💡 **Quick Tip:** Drink a glass of water and stretch your shoulders. Physical tension often adds to mental stress.",
    "💡 **Quick Tip:** Write down one small thing you can control right now, and let go of the rest for today."
]

def get_bot_response(user_input):
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity
    
    if polarity < -0.1:
        mood = "negative"
        tip = random.choice(relaxation_tips)
    elif polarity > 0.2:
        mood = "positive"
        tip = ""
    else:
        mood = "neutral"
        tip = ""
        
    reply = random.choice(responses[mood])
    if tip:
        reply += f"\n\n{tip}"
        
    return reply

st.title("💙 Student Mental Health Companion")
st.markdown("""
Welcome. I am an AI companion designed to listen and support you. 
*Note: I am an AI, not a professional counselor. If you are in crisis, please reach out to campus services or a trusted professional.*
""")
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How are you feeling today?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = get_bot_response(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
