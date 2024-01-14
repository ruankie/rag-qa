[![GitHub stars](https://img.shields.io/github/stars/ruankie/rag-qa)](https://github.com/ruankie/rag-qa/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/ruankie/rag-qa)](https://github.com/ruankie/rag-qa/commits/main)

# rag-qa

## Description

A containerised QA framework to ask questions to your documents.

## Usage
> Make sure you enter your OpenAI API key in a `.env` file as shown in `.env.example`

1. Run the backend and frontend
    ```shell
    docker compose up
    ```
2. Navigate to the frontend in your browser: http://localhost:8501/
3. Input a URL that contains content you want to ask a question about
4. Ask a question in the chat input section and wait for a response

## Development

### Dev Prerequisites
1. (Optional) [Download](https://asdf-vm.com/guide/getting-started.html#_2-download-asdf) and [install](https://asdf-vm.com/guide/getting-started.html#_3-install-asdf) [asdf](https://asdf-vm.com/) on your machine to manage the version of Python and Poetry used in this project. Once done, run `asdf install` to install the versions specified in `.tool-versions`. Alternatively, install them manually as described below:
2. [Install Poetry](https://python-poetry.org/docs/#installation) on your machine
3. [Install Python 3](https://www.python.org/downloads/) on your machine
4. Create a virtual environment for your project using the command `poetry install`. This will install all the basic dependencies specified in your `pyproject.toml` file.
