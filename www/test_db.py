#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'John Wang'

from models import User

from transwarp import db
import logging
import random

logging.basicConfig(level=logging.DEBUG)

db.create_engine(user='root', password='QQQQQQ', database='python_blog')

u = User(name='Test', admin=False, email='test_' + str(chr(random.randint(65, 90))) + '@example.com' , password='1234234', image='http://like.img')

u.insert()
print 'new user id:', u.id

u1 = User.find_first('where email=?', 'test_6@example.com')

print 'find user\'s name:', u1.name
u1.delete()

u2 = User.find_first('where email=?', 'test@example')
print 'find user:', u2
