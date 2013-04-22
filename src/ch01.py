from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='hello')
def hello_world(request):
    return Response('Hello World!')


def main():
    config = Configurator()
    config.add_route('hello', '/')
    config.scan()
    return config.make_wsgi_app()


if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
