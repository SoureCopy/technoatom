from wsgiref.simple_server import make_server
from wsgiClass import WSGIapp

http_server = make_server('localhost', 35235, WSGIapp, )
http_server.serve_forever()