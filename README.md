# GENZCHAT

**GENZCHAT** is an interactive chatbot application built using Streamlit. It offers users multiple functionalities such as chatting with the bot, participating in chatrooms, and engaging in private messaging with other users. The application is designed with a modern black-and-white theme and includes user authentication for enhanced security.

---

## Key Features

1. **User Authentication**:
   - Secure registration and login using hashed passwords.

2. **Chatbot Interaction**:
   - Chat with an AI-driven chatbot powered by Natural Language Processing (NLP).

3. **Private Messaging**:
   - Send and receive private messages from other users.

4. **Group Chatrooms**:
   - Participate in group conversations within predefined chatrooms like General, Tech Talk, Gaming, and Music.

5. **Responsive Design**:
   - Aesthetic black-and-white theme with animations and modern UI elements.

6. **Persistent Chat Logs**:
   - Chat history is saved and accessible for each user in the respective chatroom or private conversation.

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/salmasyed19/GENZCHAT.git
   cd GENZCHAT
   ```

2. **Install Dependencies**:
   Ensure you have Python installed (preferably 3.8 or higher). Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

4. **Access the Application**:
   Open your browser and go to:
   ```
   http://localhost:8501
   ```

---

## File Structure

```
GENZCHAT/
|-- app.py               # Main application file
|-- intents.json         # Intents and responses for chatbot
|-- nltk_data/           # Required NLTK data files
|-- users.csv            # User credentials database
|-- chat_log.csv         # Chat history logs
|-- logo.png             # Application logo
|-- requirements.txt     # Python dependencies
|-- README.md            # Project documentation
```

---

## Key Technologies

- **Frontend**: Streamlit for UI and interactions.
- **Backend**: Python for NLP, user authentication, and chat handling.
- **Data Storage**: CSV files for user data and chat history.
- **NLP Model**: Trained using TF-IDF vectorizer and Logistic Regression for intent detection.

---

## Customization

1. **Theme**:
   - The app uses a black-and-white theme with custom CSS. You can modify the styles in the `<style>` section of `app.py`.

2. **Chatbot Intents**:
   - Update or add new intents and responses in `intents.json` to customize the chatbot behavior.

3. **Chatrooms**:
   - Add or modify chatrooms by updating the `chat_rooms` list in `app.py`.

---

## Deployment

To deploy the app, use any cloud provider or platform that supports Streamlit. Here are two common methods:

### Heroku Deployment
1. **Install Heroku CLI** and log in.
2. Add a `Procfile` with the following content:
   ```
   web: streamlit run app.py --server.port=$PORT
   ```
3. Commit changes and push to Heroku:
   ```bash
   git add .
   git commit -m "Deploying to Heroku"
   git push heroku main
   ```

### Streamlit Cloud Deployment
1. Log in to [Streamlit Cloud](https://streamlit.io/cloud).
2. Connect your GitHub repository.
3. Deploy the application with one click.

---

## Contribution

Feel free to fork the repository and contribute to the project. Submit pull requests for any enhancements or bug fixes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

Special thanks to the Streamlit community and the creators of Scikit-learn and NLTK for providing powerful tools for developing interactive and intelligent applications.
