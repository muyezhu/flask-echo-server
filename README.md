# Setup instructions
```bash
export PIP_BREAK_SYSTEM_PACKAGES=1
sudo apt-get update
sudo apt-get install -y git unzip zip curl tar wget python3 python3-pip
/usr/bin/python3 -m pip install pytest tox poetry
/usr/bin/python3 -m poetry install
```

# Testing instructions
```bash
/usr/bin/python3 -m poetry run pytest
```
