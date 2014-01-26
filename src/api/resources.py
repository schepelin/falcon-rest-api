# -*- coding: utf-8 -*-

import json

import falcon


__all__ = (
    'UsersResource',
)


class UsersResource(object):

    def __init__(self, storage, default_limit=10):
        self.storage = storage
        self.default_limit = default_limit

    def on_get(self, req, resp):
        limit = req.get_param_as_int('limit') or self.default_limit
        offset = req.get_param_as_int('offset') or 0

        data = self.storage.users_list(offset=offset, limit=limit)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(data)

    def on_post(self, req, resp):
        pass
