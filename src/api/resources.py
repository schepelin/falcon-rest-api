# -*- coding: utf-8 -*-

import falcon


__all__ = (
    'UsersResource',
)


class UsersResource(object):

    def __init__(self, storage):
        self.storage = storage

    def on_get(self, req, resp):
        pass

    def on_post(self, req, resp):
        pass
