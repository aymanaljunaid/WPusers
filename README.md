# WPusers

WPusers is a Python tool designed to enumerate WordPress usernames from a given website. It uses multiple methods, including the WordPress REST API and author endpoint, to discover usernames.

## Features

- Enumerates WordPress usernames using the REST API.
- Falls back to author endpoint enumeration.
- User-Agent rotation to avoid detection.
- Supports proxy usage.
- Adds random delays between requests to simulate human behavior.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aymanaljunaid/WPusers.git
    
    ```bash
    cd WPusers
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script without a proxy:
    ```bash
    python3 WPusers.py <url>
    ```
    
## Run the script:
    ```bash
    python3 WPusers.py https://example.com
    ```
    ```bash
    python3 WPusers.py https://example.com http://your-proxy:port
    ```

## Disclaimer

This tool is designed for educational and security testing purposes only. Unauthorized use of this tool against websites without permission is illegal. The tool is not designed to bypass or defeat any security measures.
