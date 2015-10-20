# -*- coding: utf-8 -*-

from bottle import route, run, template, redirect, post, request
from forms import UserForm

import helpers
import settings


@route('/query/select/<db_name>')
def select(db_name):
    database = helpers.Connection(db_name)
    users = database.query(settings.QUERIES['SELECT'])
    form = UserForm()
    return template('templates/select', users=users, db_name=db_name,
                    form=form, dbs=settings.DBS)


@post('/query/insert/<db_name>')
def insert(db_name):
    form = UserForm(request.forms)
    database = helpers.Connection(db_name)
    query = (settings.QUERIES['INSERT']
             .format(form.name.data, form.surname.data, form.email.data,
                     form.phone.data, form.birthday.data))
    (database.query(query))
    redirect('/query/select/{}'.format(db_name))


@route('/')
def index():
    return template('templates/index', dbs=settings.DBS,
                    credentials=settings.CREDENTIALS)


@route('/query/delete/<db_name>/<row_id>/')
def delete(db_name, row_id):
    database = helpers.Connection(db_name)
    database.query(settings.QUERIES['DELETE'].format(row_id))
    redirect('/query/select/{}'.format(db_name))

run(host='0.0.0.0', port=80)
