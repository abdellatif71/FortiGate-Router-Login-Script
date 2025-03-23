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
    'username': 'admin',  # Ersetze mit den echten Daten
    'password': ''        # Leer, falls Default
}

try:
    response = session.post(url, headers=headers, data=urlencode(data))
    print("Status:", response.status_code)
    print("Antwort:", response.text)
except requests.exceptions.ConnectionError:
    print("Verbindung fehlgeschlagen: Kein Webserver auf Port 80 oder IP falsch.")