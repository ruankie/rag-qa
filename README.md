[![GitHub stars](https://img.shields.io/github/stars/ruankie/poetry-py-template)](https://github.com/ruankie/poetry-py-template/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/ruankie/poetry-py-template)](https://github.com/ruankie/poetry-py-template/commits/main)

# poetry-py-template

<img src="https://github.com/ruankie/poetry-py-template/assets/58558211/beac2040-3db6-4ab5-a512-ef137a563140" width="240" />

## Description

This is a minimal project template for Python projects that uses Poetry for dependency virtual environment management.

## Setup

### Prerequisites
1. (Optional) [Download](https://asdf-vm.com/guide/getting-started.html#_2-download-asdf) and [install](https://asdf-vm.com/guide/getting-started.html#_3-install-asdf) [asdf](https://asdf-vm.com/) on your machine to manage the version of Python and Poetry used in this project. Once done, run `asdf install` to install the versions specified in `.tool-versions`. Alternatively, install them manually as described below:
2. [Install Poetry](https://python-poetry.org/docs/#installation) on your machine
3. [Install Python 3](https://www.python.org/downloads/) on your machine
4. Create a virtual environment for your project using the command `poetry install`. This will install all the basic dependencies specified in your `pyproject.toml` file.

### Add Dependencies
1. You can use the following command to add dependencies to your Poetry env:
    ```shell
    poetry add <package>
    ```
2. You can also add dev dependencies by running:
    ```shell
    poetry add <package> --group dev
    ```
### General
1. Update the `LICENSE` file
2. Update the `README.md` file
3. Change the project name, description, version, and authors in `pyproject.toml`
4. Finally, once you get to this point, you might want to delete the `poetry.lock` file and re-run the following command to update your virtual environment with your new changes:
    ```shell
    poetry install
    ```

## Usage
1. Add your own scripts and modules in `src/`
2. Add your own notebooks in `notebooks/`
3. Add your own examples of environment variables used in `.env.example`
4. Add your own unit tests in `tests/`
5. Double check that you have set up your virtual env correctly by running 
    ```shell
    poetry env info
    ```
6. To open a shell inside your virtual env, run
   ```shell
    poetry shell
    ```
7. To run a command within your virtual env, prepend it with `poetry run`. For example:
   ```shell
   poetry run echo "hello from poetry env"
   ```
8. If at any point you have added more dependencies and you want it to reflect in your `poetry.lock` file, you can run 
   ```shell
   poetry update
   ```
9. To run your tests, run:
    ```shell
    poetry run pytest .
    ```
