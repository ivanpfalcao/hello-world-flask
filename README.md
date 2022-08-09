# Hello World Flask

A simple implementation of hello world script in Python - Flask


## Installation

To install the dependencies you may use conda our venv

```python
# Using conda
conda create -p "<venv-directory>" python=3.9 -y

source activate "<venv-directory>"
# depending on your installation you may use
# conda activate "<venv-directory>"

pip install -r requirements.txt
```

```python
# Using python virtualenv
python3 -m venv "<venv-directory>"

source activate "<venv-directory>"
# depending on your installation you may use
# conda activate "<venv-directory>"

pip install -r requirements.txt
```

## Running

To run the code you could simply use

```python
# Running hello world
python hello_world.py
```

If you need to change the output host or the port you may run

```python
# Running hello world with different host and port
# By Default 0.0.0.0 and 5000 respectively
python hello_world.py --host=127.0.0.1 --port=8080
```

