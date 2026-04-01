# Project Setup Guide

This guide covers how to set up and run the project using either the traditional **pip** method or the modern **uv** workflow.

---

## 🏗️ Option 1: Standard Setup (pip)

Follow these steps to manually configure your environment and install the necessary browser drivers.

### 1. Create a Virtual Environment
```bash
python -m venv .venv
```

### 2. Activate the Environment
* **Windows:**
    ```bash
    .venv\Scripts\activate
    ```
* **macOS / Linux:**
    ```bash
    source .venv/bin/activate
    ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright Firefox
```bash
playwright install firefox
```

### 5. Run the Project
```bash
python main.py
```

---

## ⚡ Option 2: Optimized Setup (uv)

If you have `uv` installed, the process is significantly faster. `uv` handles the environment creation and dependency sync automatically.

### 1. Install Playwright Firefox
```bash
uv run playwright install firefox
```

### 2. Run the Project
```bash
uv run main.py
```

---

## 🛠️ Troubleshooting
* **Playwright Errors:** If Firefox fails to launch, ensure you have run the `install` command above.
* **Environment:** Always ensure your virtual environment is active (if using the pip method) before running the script.
