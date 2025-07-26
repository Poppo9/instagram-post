# Instagram Login Automation

This project automates the login process to [Instagram](https://www.instagram.com) using Python and Selenium. It mimics human behavior to avoid bot detection, with support for randomized delays and secure credential handling.

-----

## 📁 Project Structure

```
.
├── funcs/
│   └── selenium_utils.py # Contains setup_driver function
├── main.py               # Main automation script
├── .env                  # Environment file with credentials
├── .gitignore
├── README.md
├── pyproject.toml        # Poetry configuration
└── poetry.lock
```

-----

## ⚙️ Features

  - Instagram login automation with Selenium.
  - Credentials loaded securely from the `.env` file.
  - Simulates human typing delays.
  - Designed to be modular and extensible.
  - Compatible with [Poetry](https://python-poetry.org).

-----

## 🧑‍💻 Setup Instructions

### 1\. Clone the repository

```bash
git clone https://github.com/Poppo9/instagram-post.git
cd instagram-post
```

### 2\. Install dependencies with Poetry in your venv

```bash
pip install poetry
poetry install --no-root
```

### 3\. Add your credentials

Create a `.env` file in the root directory with the following content:

```ini
IG_USER=your_instagram_username
IG_PWD=your_instagram_password
```

🔐 **Never share or commit your `.env` file.** It contains sensitive information.

### 4\. Run the script

```bash
python main.py
```