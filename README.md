# AUTO-REPLY AI CHATBOT: NARUTO

## Overview

Naruto is an automated AI chatbot designed to interact humorously within a chat application. Powered by OpenAI's GPT-3.5-turbo model, it analyzes chat history and generates witty, roast-style responses, creating an engaging and entertaining user experience.

---

## Features

### Automated Chat Interaction

* Uses `pyautogui` to automate mouse and keyboard operations, enabling seamless interaction with the chat application without manual intervention.

### Chat History Analysis

* Copies chat history from the chat application.
* Analyzes chat history to identify messages from a specific user (e.g., "Rohan Das").

### Humorous Response Generation

* Leverages OpenAI's GPT-3.5-turbo to generate roast-style, humorous replies based on the analyzed chat history.

### Clipboard Operations

* Utilizes `pyperclip` for efficient copy-paste operations to retrieve and send chat messages.

---

## Workflow

### 1. Initialization and Setup

* Clicks on the Chrome icon to open the chat application.
* Waits briefly to ensure the application is open and ready.

### 2. Chat History Retrieval

* Periodically selects and copies the chat history using automated mouse and keyboard operations.
* Retrieves the copied text from the clipboard.

### 3. Message Analysis

* Analyzes the copied chat history to determine if the last message is from a specific user (e.g., "Rohan Das").

### 4. Response Generation

* If the last message is from the target user, sends the chat history to OpenAI's GPT-3.5-turbo model to generate a humorous response.
* Copies the generated response to the clipboard.

### 5. Response Delivery

* Automates clicking on the chat input area and pastes the generated response.
* Sends the message by pressing 'Enter'.

---

## Libraries Used

1. **`pyautogui`:** Automates mouse and keyboard interactions.
2. **`time`:** Adds delays between operations.
3. **`pyperclip`:** Handles clipboard operations for copying and pasting text.
4. **`openai`:** Interfaces with OpenAI's GPT-3.5-turbo model for AI-driven responses.

---

## How to Use

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/auto-reply-chatbot.git
   cd auto-reply-chatbot
   ```

2. **Install Dependencies**
   Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Key**

   * **OpenAI API Key:** Obtain your key from OpenAI and configure it as an environment variable or within a configuration file.

4. **Run the Application**

   ```bash
   python naruto_chatbot.py
   ```

5. **Interact with Naruto**

   * Ensure the chat application is open.
   * Watch as Naruto automates interactions, generates witty replies, and keeps the chat lively.

---

## Future Enhancements

* Expand compatibility with multiple chat platforms.
* Improve chat history parsing for nuanced context understanding.
* Add a configuration interface for customizing responses.
* Enhance AI-generated humor by training with domain-specific data.

---

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to submit a pull request or open an issue.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

* OpenAI for the GPT-3.5-turbo API.
* Developers of `pyautogui`, `pyperclip`, and other libraries used in this project.
