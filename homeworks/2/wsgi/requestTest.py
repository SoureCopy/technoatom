import requests

for elem in range(5):
    response = requests.get('http://localhost:35235/')
    print(response.status_code)
    print(response.text)