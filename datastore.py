#!/usr/bin/env python

__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

from google.appengine.ext import db


class Posts(db.Model):
    ID = db.IntegerProperty()
    title = db.StringProperty()
    author = db.StringProperty()
    timestamp = db.DateTimeProperty(auto_now=True)
    content = db.StringProperty()


class Comments(db.Model):
    ID = db.IntegerProperty()
    comment = db.StringProperty()
    author = db.StringProperty()
    timestamp = db.DateTimeProperty(auto_now=True)