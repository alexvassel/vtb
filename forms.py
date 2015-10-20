# -*- coding: utf-8 -*-

import wtforms


class UserForm(wtforms.Form):
    name = wtforms.StringField(u'Имя')
    surname = wtforms.StringField(u'Фамилия')
    email = wtforms.StringField(u'Электронная почта')
    phone = wtforms.StringField(u'Телефон')
    birthday = wtforms.StringField(u'День рождения')
