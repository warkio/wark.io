import os

PACKAGE_ROOT = os.path.dirname(os.path.abspath(__file__))

TEMPLATES_DIRECTORY = os.path.abspath(os.path.join(PACKAGE_ROOT, '..', 'templates'))
PUBLIC_DIRECTORY = os.path.abspath(os.path.join(PACKAGE_ROOT, '..', 'public'))
MIGRATIONS_DIRECTORY = os.path.abspath(os.path.join(PACKAGE_ROOT, '..', 'migrations'))

DEBUG = os.getenv('WARK_PRODUCTION', '0') != '1'

HOSTNAME = os.getenv('WARK_BIND_HOSTNAME', '127.0.0.1')
PORT = int(os.getenv('WARK_BIND_PORT', 8080))

TITLE = 'wark'
