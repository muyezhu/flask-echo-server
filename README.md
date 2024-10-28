# Setup instructions
```bash
export PIP_BREAK_SYSTEM_PACKAGES=1
/usr/bin/python3 -m pip install pytest tox poetry
/usr/bin/python3 -m poetry install
```

# Testing instructions
```bash
/usr/bin/python3 -m poetry run pytest
```
