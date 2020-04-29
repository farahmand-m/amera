import argparse
import os
import signal
import sys

from flask import Flask
from flask import render_template
from gevent import signal as sig
from gevent.pywsgi import WSGIServer


def parse_args(arguments=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--host', type=str, default='127.0.0.1', help='Host')
    parser.add_argument('-p', '--port', type=int, default=5000, help='Port Number')
    parser.add_argument('-l', '--log', action='store_true', help='Logs the requests to stdout.')
    return parser.parse_args(arguments)


def create_app(args):
    filepath = os.path.dirname(__file__)

    configurations = {
        # NuxtJS static files need to be served by Flask.
        'static_url_path': '/_nuxt/',
        'static_folder': os.path.join(filepath, '..', 'built', '_nuxt'),
        'template_folder': os.path.join(filepath, '..', 'built')
    }
    app = Flask(__name__, **configurations)

    # Index and all unregistered routes must be handled by the NuxtJS app.
    @app.route('/')
    @app.route('/<path:path>')
    def nuxtjs(path=None):
        return render_template('index.html')

    return app


def setup():
    args = parse_args()

    app = create_app(args)
    server = WSGIServer((args.host, args.port), app, log='default' if args.log else None)

    # On a termination or interrupt signal, we want the server to end gracefully!
    def graceful_exit(*args):
        print('Terminating the server now...', file=sys.stderr)
        server.stop()

    sig.signal(signal.SIGTERM, graceful_exit)
    sig.signal(signal.SIGINT, graceful_exit)

    print('Running Amera at http://{}{}{}.'.format(args.host, ':' if args.port != 80 else '', args.port), file=sys.stderr)
    server.serve_forever()
