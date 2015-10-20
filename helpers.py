# -*- coding: utf-8 -*-
import importlib
from settings import DBS


class Connection(object):
    def __init__(self, db_name='postgres'):
        if db_name not in DBS:
            raise ValueError('this db is not supported')
        self.db_name = db_name

    def _get_connection(self):
        module = importlib.import_module(DBS[self.db_name]['module'])
        connection = module.connect(DBS[self.db_name]['connection_string'])
        return connection

    def query(self, query):
        connection = self._get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        try:
            result = cursor.fetchall()
        except Exception:
            result = []
        connection.commit()
        cursor.close()
        connection.close()
        return result
