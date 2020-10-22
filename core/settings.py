import os
from .urls import URL_PATTERNS
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from core.views import MainView
from tornado_sqlalchemy import SQLAlchemy, SessionMixin

# Define port
define('port', default=8888, help='port to listen on')

# Define database
define("mysql_host", default="mysql://root:root@localhost:3306/tornado", help="Main user DB")

factory = SessionMixin.make_session(options.mysql_host)


def db_settings(database_url: str = options.mysql_host) -> SQLAlchemy:
    return SQLAlchemy(url=database_url)


SQLAlchemyInstance = db_settings()


def main():
    """Construct and serve the tornado application."""
    http_server = HTTPServer(URL_PATTERNS)
    http_server.listen(options.port)
    print('Listening on http://localhost:%i' % options.port)
    IOLoop.current().start()
