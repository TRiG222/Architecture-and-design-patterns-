from trig_framework.main import Framework
from urls import routes, front
from wsgiref.simple_server import make_server

app = Framework(routes, front)

with make_server('', 8888, app) as httpd:
    print('start server on :8888 port')
    httpd.serve_forever()
