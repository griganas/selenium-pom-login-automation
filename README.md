# Selenium POM Login Automation

This project demonstrates automated login testing using **Selenium WebDriver**, **Pytest**, and the **Page Object Model (POM)** design pattern.

## Features

- ✅ Login Success Test
- ❌ Login Failure Tests (with invalid credentials using parametrize)
- Page Object Model structure
- Pytest fixtures in `conftest.py`

## Technologies

- Python
- Selenium
- Pytest
- POM design

## How to run

```bash
pytest test_login_success.py
pytest test_login_failure.py