import waitress

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='hello')
def hello_world(request):
    return Response('Hello World!')


@view_config(route_name='bye')
def goodbye_world(request):
    return Response('Goodbye World!')


def main():
    config = Configurator()
    config.add_route('hello', '/')
    config.add_route('bye', '/bye')
    config.scan()
    return config.make_wsgi_app()


if __name__ == '__main__':
    app = main()
    waitress.serve(app, host='0.0.0.0', port='8080')
