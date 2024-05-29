NAME : MEGHA BHAT
EMAIL : meghajbhat@gmail.com


# ChatGPT API Simple Chatbot

This project is a simple chatbot that uses OpenAI's GPT-3.5-turbo model. 
It consists of a client and a server script that communicate over HTTP. 
The server handles the interaction with the OpenAI API, and the client provides a simple command-line interface for users to interact with the chatbot.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Features

- Simple and intuitive command-line interface for chatting with GPT-3.5-turbo.
- Proxy server that handles API requests and responses.
- Maintains conversation history for context-aware responses.
- Secure communication with OpenAI API.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/meghajbhat/AIML-Project-Series1.git
    cd AIML-Project-Series1
    ```

2. Navigate to the `ChatGPT-API-Simple-Chatbot` directory:
    ```sh
    cd "ChatGPT-API-Simple-Chatbot"
    ```

3. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running the Server

1. Open a terminal and navigate to the project directory.
2. Start the server by running:
    ```sh
    python basicserver.py
    ```
3. The server will start on port `65432`.

### Running the Client

1. Open another terminal and navigate to the project directory.
2. Start the client by running:
    ```sh
    python basicclient.py
    ```
3. Interact with the chatbot by typing your questions. Type `exit` to quit the client.

## Configuration

1. **OpenAI API Key**:
   - Replace `'YOUR_OPEN_API_KEY_HERE'` in `basicserver.py` with your actual OpenAI API key.

2. **Model Configuration**:
   - The model used is `gpt-3.5-turbo-1106`. You can change this in the `query_chatgpt` method if you want to use a different model.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

1. Fork the Project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## Acknowledgements

- [OpenAI](https://www.openai.com) for providing the GPT-3.5-turbo model.
- The Python community for various useful libraries.

---

Feel free to open an issue if you find a bug or have a question. Happy coding!
