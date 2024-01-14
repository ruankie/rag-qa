[![GitHub stars](https://img.shields.io/github/stars/ruankie/rag-qa)](https://github.com/ruankie/rag-qa/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/ruankie/rag-qa)](https://github.com/ruankie/rag-qa/commits/main)

# rag-qa

## Description

A containerised QA framework to ask questions to your documents.

## Setup

### Prerequisites
1. (Optional) [Download](https://asdf-vm.com/guide/getting-started.html#_2-download-asdf) and [install](https://asdf-vm.com/guide/getting-started.html#_3-install-asdf) [asdf](https://asdf-vm.com/) on your machine to manage the version of Python and Poetry used in this project. Once done, run `asdf install` to install the versions specified in `.tool-versions`. Alternatively, install them manually as described below:
2. [Install Poetry](https://python-poetry.org/docs/#installation) on your machine
3. [Install Python 3](https://www.python.org/downloads/) on your machine
4. Create a virtual environment for your project using the command `poetry install`. This will install all the basic dependencies specified in your `pyproject.toml` file.

## Usage
1. Add your own scripts and modules in `src/`
2. Add your own notebooks in `notebooks/`
3. To run your tests, run:
    ```shell
    poetry run pytest .
    ```
