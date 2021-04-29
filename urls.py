from datetime import date
from views import Index, Blog


# front controller
def secret_front(request):
    request['data'] = date.today()


def other_front(request):
    request['key'] = 'key'


front = [secret_front, other_front]

routes = {
    '/': Index(),
    '/blog/': Blog()
}
