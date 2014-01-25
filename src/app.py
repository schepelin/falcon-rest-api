# -*- coding: utf-8 -*-

from wsgiref import simple_server

import falcon

from storage import SQLiteStorage
from api.resources import UsersResource


__all__ = (
    'application',
)


application = falcon.API()

db = SQLiteStorage(db_name='db.sqlite')

users = UsersResource(storage=db)

application.add_route('/users', users)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, application)
    httpd.serve_forever()
