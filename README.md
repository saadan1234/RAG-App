# Ollama Server Setup and Application Run Instructions

This guide will walk you through the steps to set up the Ollama server, pull the necessary models, and run the application.

## Prerequisites

- Ensure you have Git installed on your system.
- Python and pip should be installed on your machine.
- A terminal or command prompt to run the commands.

## Instructions

### 1. Download the Repository

First, download or clone the repository containing the application code.

```sh
git clone <repository_url>
cd <repository_folder>
```

### 2. Download Ollama Server
Visit the Ollama website to download the Ollama server. Follow the instructions on the site for installation.

### 3. Pull the Embedding Model
Choose and pull an embedding model. Here, mxbai-embed-large is recommended, but you can choose another if you prefer.

```sh
ollama pull mxbai-embed-large
```

### 4. Pull the Response Generation Model
Next, pull the response generation model. You can use gemma2, llama3, or another model of your preference.

```sh
ollama pull gemma2
```

### 5. Ensure Models in Code Match
Verify that the models specified in your code match the ones you have pulled onto your device. Open your application code and check the model names.

### 6. Run the Ollama Server
Start the Ollama server in one terminal window.

```sh
ollama serve
```

### 7. Run the Application
Open another terminal window and navigate to the directory containing app.py. Run the application on localhost port 5500.

```sh
python app.py
```

### 8. Response Time
Please note that the response time may vary from 1 to 15 minutes, depending on your device's specifications.

# Contributing
Feel free to contribute to this project by opening issues or submitting pull requests.
