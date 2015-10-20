# coding=utf-8

import os

os.environ['NLS_LANG'] = '_.AL32UTF8'

CREDENTIALS = {'common': dict(table_name='users'),
               'mssql': dict(host='__mssql_ip__', port='1433', db_name='vtb',
                             username='vtb_demo', password='vtb_demo'),
               'oracle': dict(host='__oracle_ip__', port='1521', db_name='XE',
                              username='vtb_demo', password='vtb_demo')}

QUERIES = {'SELECT': ('SELECT * FROM {}'
                      .format(CREDENTIALS['common']['table_name'])),
           'DELETE': ('DELETE FROM {} WHERE id={}'
                      .format(CREDENTIALS['common']['table_name'], {})),
           'INSERT': (("INSERT INTO {} (name,surname,email,phone,birthday) "
                       "VALUES ('{}', '{}', '{}', '{}', '{}')")
                      .format(CREDENTIALS['common']['table_name'],
                              {}, {}, {}, {}, {}))}

DBS = {'mssql':
       {'module': 'pypyodbc', 'name': 'Microsoft SQL Server',
        'connection_string': ('Driver=FreeTDS;Server={};port={};'
                              'uid={};pwd={};database={}'
                              .format(CREDENTIALS['mssql']['host'],
                                      CREDENTIALS['mssql']['port'],
                                      CREDENTIALS['mssql']['username'],
                                      CREDENTIALS['mssql']['password'],
                                      CREDENTIALS['mssql']['db_name']))},
       'oracle':
       {'module': 'cx_Oracle', 'name': 'Oracle',
        'connection_string': ('{}/{}@{}:{}/{}'
                              .format(CREDENTIALS['oracle']['username'],
                                      CREDENTIALS['oracle']['password'],
                                      CREDENTIALS['oracle']['host'],
                                      CREDENTIALS['oracle']['port'],
                                      CREDENTIALS['oracle']['db_name']))}}

