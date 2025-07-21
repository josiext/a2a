# Agent-to-Agent Project

## Setup Instructions

### 1. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt
```

### 3. Run the Project

```bash
fastapi dev main.py
```

### 4. Development

- Add your dependencies to `requirements.txt`
- Follow PEP 8 style guidelines
- Add tests in a `tests/` directory
- Use meaningful commit messages following Conventional Commits

### 5. Deactivate Virtual Environment

```bash
deactivate
```

## Project Structure

```
agent-to-agent/
├── main.py              # Main entry point
├── requirements.txt     # Project dependencies
├── README.md           # This file
├── .gitignore          # Git ignore patterns
└── venv/               # Virtual environment (created after setup)
``` 