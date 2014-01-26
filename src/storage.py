# -*- coding: utf-8 -*-

import sqlite3
import logging


__all__ = (
    'SQLiteStorage',
)


class SQLiteStorage(object):
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.logger = logging.getLogger('app.' + __name__)
        self.create_tables_if_not_exists()

    def create_tables_if_not_exists(self):
        cursor = self.connection.cursor()

        try:
            cursor.execute('CREATE TABLE Users(Id INT PRIMARY_KEY NOT NULL, Name CHAR(30) NOT NULL);')
        except sqlite3.OperationalError:
            self.logger.info('Table "Users" already exists')

        try:
            cursor.execute(
                'CREATE TABLE Posts(Id INT PRIMARY_KEY NOT NULL, User_Id INT '
                'NOT NULL, Title TEXT NOT NULL, Content TEXT NOT NULL);'
            )
        except sqlite3.OperationalError:
            self.logger.info('Table "Posts" already exists')

    def commit(self):
        self.connection.commit()

    def insert(self, query, *params):
        try:
            with self.connection:
                self.connection.execute(query, params)
        except sqlite3.IntegrityError as error:
            self.logger.error('Fail execute: %s', error)

    def users_list(self, limit, offset=0):
        limit = limit
        cursor = self.connection.cursor()

        users = []
        try:
            cursor.execute('SELECT Id, Name FROM Users ORDER BY Id ASC LIMIT ? OFFSET ?;', (limit, offset))
        except sqlite3.IntegrityError as error:
            self.logger.error('Fail execute: %s', error)
        else:
            data = cursor.fetchall()
            users = [dict(id=item[0], name=item[1]) for item in data]
        return users
