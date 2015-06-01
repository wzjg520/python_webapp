#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'John Wang'

'''
Models for user, blog, comment
'''

import time
import uuid

from transwarp.db import next_id
from transwarp.orm import Model, StringField, BooleanField, IntegerField, FloatField, TextField

import logging

logging.basicConfig(level=logging.DEBUG)

class User(Model):
    __table__ = 'user'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(updateable=False, ddl='varchar(50)')
    password = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    create = FloatField(updateable=False, default=time.time)


class Blog(Model):
    __table__ = 'blog'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(updateable=False, ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(50)')
    content = TextField()
    create = FloatField(updateable=False, default=time.time)


class Comment(Model):
    __table__ = 'comment'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(updateable=False, ddl='varchar(50)')
    user_id = StringField(updateable=False, ddl='varchar(50)')
    user_name = StringField(ddl='varchar(500)')
    content = TextField()
    create = FloatField(updateable=False, default=time.time)
