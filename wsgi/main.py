from wsgiref.simple_server import make_server
from wsgiClass import WSGIapp
import requests

http_server = make_server('localhost', 35235, WSGIapp, )
http_server.serve_forever()
for elem in range(5):
    response = requests.get('http://localhost:35235/')
    print(response.status_code)
    print(response.text)