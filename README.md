[![GitHub stars](https://img.shields.io/github/stars/ruankie/rag-qa)](https://github.com/ruankie/rag-qa/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/ruankie/rag-qa)](https://github.com/ruankie/rag-qa/commits/main)

# rag-qa

## Description

A free containerised QA framework to ask questions to your documents.

## Demo
![demo](./assets/demo.gif)


## Usage

> Note: The first time you run this, it might take a while to build all the images and download the embedding models.

1. You will need an API key from OpenAI or Google. You can create one for free here:
    - [OpenIA](https://platform.openai.com/account/api-keys) - to use models like GPT4
    - [Google](https://ai.google.dev/) - to use models like Gemini (Recommended since it's free)
2. Set up your API keys in a file called `.env` (see `.env.example` for an example)


3. Now set up the backend and frontend
    ```shell
    docker compose up
    ```
4. Navigate to the frontend in your browser: http://localhost:8501/
5. Input a URL that contains content you want to ask a question about
6. Ask a question in the chat input section and wait for a response

## Development

1. (Optional) [Download](https://asdf-vm.com/guide/getting-started.html#_2-download-asdf) and [install](https://asdf-vm.com/guide/getting-started.html#_3-install-asdf) [asdf](https://asdf-vm.com/) on your machine to manage the version of Python and Poetry used in this project. Once done, run `asdf install` to install the versions specified in `.tool-versions`. Alternatively, install them manually as described below:
2. [Install Poetry](https://python-poetry.org/docs/#installation) on your machine
3. [Install Python 3](https://www.python.org/downloads/) on your machine
4. Create a virtual environment for your project using the command `poetry install`. This will install all the basic dependencies specified in your `pyproject.toml` file.
5. Set up your API keys in a file called `.env` (see `.env.example` for an example)