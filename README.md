FortiGate Router Login Script

This script attempts to log in to a FortiGate router or web-based device located at 192.168.1.1 by sending a POST request to the /logincheck endpoint.

Requirements

Python 3

requests library (install using pip install requests)

How It Works

Creates a session using requests.Session() to maintain cookies and session data.

Defines custom headers, including User-Agent and Content-Type.

Sends a POST request with the login credentials (admin as username, password left empty by default).

Handles connection errors if the server is unreachable.

Installation

Clone this repository or download the script.

Install dependencies:

pip install requests

Run the script:

python script.py

Code Example

import requests
from urllib.parse import urlencode

session = requests.Session()
headers = {
    'Host': '192.168.1.1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'http://192.168.1.1/logincheck'
data = {
    'username': 'admin',  # Replace with actual credentials
    'password': ''        # Leave empty if default
}

try:
    response = session.post(url, headers=headers, data=urlencode(data))
    print("Status:", response.status_code)
    print("Response:", response.text)
except requests.exceptions.ConnectionError:
    print("Connection failed: No web server on port 80 or incorrect IP address.")

Troubleshooting

If the login fails, check if the FortiGate router uses a different IP (e.g., 192.168.0.1).

FortiGate routers may require a CSRF token for authentication.

Ensure the credentials are correct.

Disclaimer

This script is intended for educational purposes only. Do not use it without proper authorization.

