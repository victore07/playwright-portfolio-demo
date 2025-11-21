# Playwright Python Automation Framework

A robust, scalable test automation framework built using **Python**, **Playwright**, and **Pytest**. This project demonstrates modern end-to-end (E2E) testing practices, utilizing the **Page Object Model (POM)** design pattern.

The framework is currently configured to test the [SauceDemo](https://www.saucedemo.com/) e-commerce sandbox.

## Tech Stack

* **Language:** Python 3.10+
* **Framework:** Playwright (Sync API)
* **Test Runner:** Pytest
* **Design Pattern:** Page Object Model (POM)

## Project Structure

```text
playwright-portfolio-demo/
├── pages/                 # Page Object classes
│   ├── login_page.py      # Encapsulation of the Login page
├── tests/                 # Test scripts
│   ├── test_login.py      # Tests verifying authentication flows
├── conftest.py            # Pytest fixtures
├── pytest.ini             # Pytest configuration settings
├── requirements.txt       # Project dependencies
└── README.md              # Documentation
```

## Key Features

* **Page Object Model:** UI logic is separated from test logic, making tests readable and easy to update if UI selectors change.
* **Pytest Fixtures:** Efficient browser instance management using `conftest.py` to handle setup and teardown automatically.
* **Robust Locators:** Uses resilient Playwright selectors (e.g., `data-test` attributes) rather than brittle XPaths.

## Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR-USERNAME/playwright-portfolio-demo.git
    cd playwright-portfolio-demo
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    # Windows: venv\Scripts\activate
    # Mac/Linux: source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

## Running Tests

**Run all tests (Headless):**
```bash
pytest
```

**Run tests with UI (Headed):**
```bash
pytest --headed
```

## Author

**Technical QA Engineer**
[www.linkedin.com/in/victore07](www.linkedin.com/in/victore07)