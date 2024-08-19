# Testify - Universal Test Automation Framework

**Testify** is a powerful Python-based automation framework designed for both web and mobile application testing. Leveraging **Selenium** for web automation and **Appium** for mobile testing, Testify is designed with flexibility, modularity, and ease of use in mind. It features a **Page Object Model (POM)** architecture, robust logging, and exception handling mechanisms, making it suitable for a wide range of testing scenarios.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Logging and Reports](#logging-and-reports)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview

Testify aims to streamline and automate testing for both web and mobile platforms, providing a **scalable** and **configurable** framework that can be integrated into any project. Whether you're performing functional tests on a web browser or running mobile tests on emulators or real devices, Testify’s unified structure enables you to manage all your tests in one place. 

This framework is ideal for **QA teams**, **developers**, and **automation engineers** looking for a comprehensive and easy-to-extend test suite.

## Features

- **Cross-Platform Support**: Web automation using **Selenium** and mobile automation using **Appium**.
- **Page Object Model (POM)**: Ensures modular and maintainable test scripts.
- **Extensive Logging**: Provides detailed logging with configurable verbosity levels.
- **Robust Exception Handling**: Graceful handling of test errors with informative messages.
- **JSON-Based Configuration**: Easily manage project settings and configurations.
- **Parallel Execution**: Run multiple tests concurrently to save time.
- **Extensible**: Supports adding new modules and extending test coverage with ease.
- **Detailed Test Reports**: Automatically generates reports after test execution.
  
## Installation

To install and configure **Testify**, follow the steps below:

### Prerequisites

- Python 3.7 or later
- Selenium
- Appium (for mobile automation)
- WebDriver (ChromeDriver, GeckoDriver, etc.)
- Appium server and mobile device emulators (for mobile testing)

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Pirate-Emperor/testify.git
    cd testify
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure WebDriver & Appium:**  
   Set up the WebDriver for your browser (e.g., ChromeDriver for Chrome) and ensure that the Appium server is running.

## Usage

1. **Run Web Tests:**

    Testify supports web testing using Selenium. To execute web tests, follow this command:

    ```bash
    python -m unittest discover tests/web_tests
    ```

2. **Run Mobile Tests:**

    For mobile automation using Appium:

    ```bash
    python -m unittest discover tests/mobile_tests
    ```

3. **Configuration Management:**

    Update your project configuration by editing the `config.json` file in the project root. This file includes all the settings for both web and mobile test environments.

4. **Logging and Reports:**

    Logs and reports are stored under the `logs/` and `reports/` directories, respectively. After test execution, detailed HTML reports are generated for review.

## Project Structure

The following structure highlights the main components of Testify:

```bash
testify/
  ├─ config/
  │  ├─ __init__.py
  │  └─ config.json
  ├─ pages/
  │  ├─ mobile_pages/
  │  │  ├─ __init__.py
  │  │  └─ base_mobile_page.py
  │  ├─ web_pages/
  │  │  ├─ __init__.py
  │  │  └─ base_web_page.py
  │  ├─ __init__.py
  │  └─ base_page.py
  ├─ tests/
  │  └─ conftest.py
  ├─ utils/
  │  ├─ __init__.py
  │  ├─ config_parser.py
  │  ├─ driver_setup.py
  │  ├─ logging_config.py
  │  ├─ mobile_driver_setup.py
  │  └─ web_driver_setup.py
  ├─ LICENSE
  └─ README.md
```

## Logging and Reports

- **Logging**: Testify comes with detailed logging, capturing every action performed during the test execution. Logs are automatically saved in the `logs/` directory with timestamps for easier debugging.
  
- **Reports**: After each test execution, an HTML report is generated in the `reports/` directory, summarizing test results (pass, fail, error) along with screenshots of failures (if any).

## Configuration

Testify utilizes a JSON configuration file to manage different aspects of the test environment, making it easy to customize and adapt to various projects.

### Example `config.json`:

```json
{
  "web": {
    "browser": "chrome",
    "headless": false,
    "timeout": 30
  },
  "mobile": {
    "platformName": "Android",
    "deviceName": "Pixel_3",
    "app": "path/to/your/app.apk",
    "automationName": "UiAutomator2"
  },
  "logging": {
    "level": "INFO",
    "file": "logs/testify.log"
  }
}
```

## Contributing

Contributions to **Testify** are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the Pirate-Emperor License. See the [LICENSE](LICENSE) file for details.

## Author

**Pirate-Emperor**

[![Twitter](https://skillicons.dev/icons?i=twitter)](https://twitter.com/PirateKingRahul)
[![Discord](https://skillicons.dev/icons?i=discord)](https://discord.com/users/1200728704981143634)
[![LinkedIn](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/piratekingrahul)

[![Reddit](https://img.shields.io/badge/Reddit-FF5700?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/u/PirateKingRahul)
[![Medium](https://img.shields.io/badge/Medium-42404E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@piratekingrahul)

- GitHub: [Pirate-Emperor](https://github.com/Pirate-Emperor)
- Reddit: [PirateKingRahul](https://www.reddit.com/u/PirateKingRahul/)
- Twitter: [PirateKingRahul](https://twitter.com/PirateKingRahul)
- Discord: [PirateKingRahul](https://discord.com/users/1200728704981143634)
- LinkedIn: [PirateKingRahul](https://www.linkedin.com/in/piratekingrahul)
- Skype: [Join Skype](https://join.skype.com/invite/yfjOJG3wv9Ki)
- Medium: [PirateKingRahul](https://medium.com/@piratekingrahul)

---
