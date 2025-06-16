# MEGA PROJECT : AUTO-REPLY AI CHATBOT

## Description

This project automates interactions with a chat application, specifically designed to analyze chat history and generate humorous responses using OpenAI's GPT-3.5-turbo model. The virtual assistant, named **Naruto**, specializes in roasting people in a funny way, based on the chat history.

---

## Features

1. **Automated Chat Interaction**
   Utilizes `pyautogui` to perform mouse and keyboard operations, automating chat interactions without manual effort.

2. **Chat History Analysis**
   Copies chat history from the chat application and determines if the last message was sent by a specific user (e.g., "Rohan Das").

3. **Humorous Response Generation**
   Integrates with OpenAI's GPT-3.5-turbo to generate funny, roast-style responses based on the analyzed chat history.

4. **Clipboard Operations**
   Uses `pyperclip` to copy and paste text, facilitating chat message retrieval and response insertion.

---

## Workflow

### 1. Initialization and Setup

* Open the chat application by clicking the Chrome icon.
* Ensure the application is fully loaded and ready for interaction.

### 2. Chat History Retrieval

* Periodically copy chat history by selecting the chat area and using the copy shortcut.
* Retrieve the copied text from the clipboard.

### 3. Message Analysis

* Analyze the chat history to determine if the last message is from a specific user (e.g., "Rohan Das").
* If the target user is identified, send the chat history to OpenAI's GPT-3.5-turbo for humorous response generation.

### 4. Generate and Send Response

* Copy the generated response to the clipboard.
* Paste the response in the chat input area and press 'Enter' to send it.

---

## Libraries Used

1. **pyautogui**: Automates mouse and keyboard interactions.
2. **time**: Adds delays between operations to ensure smooth execution.
3. **pyperclip**: Handles clipboard operations for text retrieval and insertion.
4. **openai**: Interfaces with OpenAI's GPT-3.5-turbo model for response generation.

---

## How It Works

1. The bot initializes and prepares for interaction with the chat application.
2. Periodically retrieves the chat history using `pyautogui` and `pyperclip`.
3. Analyzes the chat history to identify the last message sender.
4. If the sender matches the target user, the bot generates a humorous response using OpenAI's GPT-3.5-turbo.
5. The bot sends the response back to the chat application, completing the interaction loop.

---

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repo/auto-reply-ai-chatbot.git
   cd auto-reply-ai-chatbot
   ```

2. **Install Dependencies**
   Install the required Python libraries:

   ```bash
   pip install pyautogui pyperclip openai
   ```

3. **Configure OpenAI API**

   * Sign up at [OpenAI](https://platform.openai.com/).
   * Generate an API key and add it to the script.

4. **Run the Bot**
   Execute the script to start the chatbot:

   ```bash
   python auto_reply_chatbot.py
   ```

---

## Contributions

Contributions are welcome! Feel free to fork this repository, submit issues, or create pull requests to enhance the project.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

* Thanks to [OpenAI](https://openai.com/) for the amazing GPT-3.5-turbo API.
* Inspired by the humorous creativity of Naruto-style roasting.
