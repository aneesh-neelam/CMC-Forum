#!/usr/bin/env python

__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

import os

import jinja2
import webapp2

import datastore


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        posts = datastore.Posts.all()
        postList = []
        for post in posts:
            postList.append({'ID': post.ID, 'title': post.title, 'author': post.author, 'timestamp': post.timestamp})
        template_values = {
            'postList': postList
        }
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))

    def post(self):
        title = self.request.get('title')
        author = self.request.get('author')
        content = self.request.get('content')
        p = datastore.Posts.all()
        count = 0
        for x in p:
            count += 1
        ID = count + 1
        newUser = datastore.Posts(ID=ID, title=title, author=author, content=content)
        newUser.put()

        posts = datastore.Posts.all()
        postList = []
        for post in posts:
            postList.append({'ID': post.ID, 'title': post.title, 'author': post.author, 'timestamp': post.timestamp})
        template_values = {
            'postList': postList
        }
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))


class PostHandler(webapp2.RequestHandler):
    def get(self):
        postID = int(self.request.get('id'))
        p = datastore.Posts.all()
        c = datastore.Comments.all()
        comments = []
        for x in c:
            if x.ID == postID:
                comments.append(x)
        for x in p:
            if x.ID == postID:
                template_values = {
                    'postID': postID,
                    'postTitle': x.title,
                    'postAuthor': x.author,
                    'timestamp': x.timestamp,
                    'postContent': x.content,
                    'postComments': comments
                }
                template = JINJA_ENVIRONMENT.get_template('templates/post.html')
                self.response.write(template.render(template_values))

    def post(self):
        postID = int(self.request.get('id'))
        author = self.request.get('author')
        comment = self.request.get('comment')
        newComment = datastore.Comments(ID=postID, comment=comment, author=author)
        newComment.put()

        p = datastore.Posts.all()
        c = datastore.Posts.all()
        comments = []
        for x in c:
            if x.ID == postID:
                comments.append(x)
        for x in p:
            if x.ID == postID:
                template_values = {
                    'postID': postID,
                    'postTitle': x.title,
                    'postAuthor': x.author,
                    'timestamp': x.timestamp,
                    'postContent': x.content,
                    'postComments': comments
                }
                template = JINJA_ENVIRONMENT.get_template('templates/post.html')
                self.response.write(template.render(template_values))