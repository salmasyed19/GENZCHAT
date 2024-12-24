import os
import json
import datetime
import csv
import hashlib
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# SSL fix for nltk
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import nltk
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents
file_path = os.path.abspath("./intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)

# Prepare model
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

# Bot response function
def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

# Password hashing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# User management
def create_user(username, password):
    if not os.path.exists('users.csv'):
        with open('users.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Password'])
    with open('users.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([username, hash_password(password)])

def verify_user(username, password):
    with open('users.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if row[0] == username and row[1] == hash_password(password):
                return True
    return False

# Private chat management
def save_private_message(sender, recipient, message):
    if not os.path.exists('private_chats.csv'):
        with open('private_chats.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Sender', 'Recipient', 'Message', 'Timestamp'])
    with open('private_chats.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([sender, recipient, message, datetime.datetime.now()])

def get_private_chat_history(user1, user2):
    history = []
    if os.path.exists('private_chats.csv'):
        with open('private_chats.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                if (row[0] == user1 and row[1] == user2) or (row[0] == user2 and row[1] == user1):
                    history.append((row[0], row[2], row[3]))
    return history

# Streamlit app
st.title("GENZ CHAT")
menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

if choice == "Register":
    st.subheader("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if password == confirm_password and username and password:
        create_user(username, password)
        st.success("Account created successfully! You can now log in.")

elif choice == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if username and password:
        if verify_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid credentials.")

if st.session_state.logged_in:
    tab1, tab2, tab3 = st.tabs(["Chatbot", "Private Chat", "Chatroom"])

    # Chatbot tab
    with tab1:
        st.subheader("Chat with the Bot")
        user_input = st.text_input("Type your message:")
        if user_input:
            response = chatbot(user_input)
            st.write(f"**Bot:** {response}")

    # Private chat tab
    with tab2:
        st.subheader("Private Messaging")
        users = []
        with open('users.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            users = [row[0] for row in csv_reader if row[0] != st.session_state.username]

        recipient = st.selectbox("Select a user to chat with", users)

        if recipient:
            st.write(f"Chatting with **{recipient}**")

            chat_history = get_private_chat_history(st.session_state.username, recipient)
            for sender, message, timestamp in chat_history:
                st.write(f"**{sender} ({timestamp}):** {message}")

            private_message = st.text_input("Type your message:", key="private")
            if private_message:
                save_private_message(st.session_state.username, recipient, private_message)
                st.success("Message sent!")

    # Chatroom tab
    with tab3:
        st.subheader("Chatroom")
        chatrooms = ["General", "Tech Talk", "Gaming", "Music"]
        chatroom = st.selectbox("Select Chatroom", chatrooms)

        st.write(f"Welcome to the **{chatroom}** chatroom!")

        if not os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'w', newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(['User', 'Message', 'Timestamp', 'Chatroom'])

        with open('chat_log.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                if row[3] == chatroom:
                    st.write(f"**{row[0]} ({row[2]}):** {row[1]}")

        chat_message = st.text_input("Type your message:", key="chatroom")
        if chat_message:
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([st.session_state.username, chat_message, datetime.datetime.now(), chatroom])
            st.success("Message sent!")
