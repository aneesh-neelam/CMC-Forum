#!/usr/bin/env python

__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

import webapp2

import handlers


app = webapp2.WSGIApplication([
                                  ('/', handlers.IndexHandler),
                                  ('/post', handlers.PostHandler)
                              ], debug=True)
