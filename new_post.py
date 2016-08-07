#!/bin/env python
import datetime
import os
import os.path
import shutil

PATH = os.path.dirname(os.path.abspath(__file__))
TODAY_PATH = os.path.join(PATH, 'today')

now = datetime.datetime.now()
title = input('title: ')

article = open('templates/article.rst').read()
article = article.replace('{{ title }}', title)
article = article.replace('{{ splitter }}', '='*len(title))
article = article.replace('{{ date }}', now.strftime('%Y-%m-%d %H:%M'))

ARTICLE_PATH = os.path.join(PATH, 'content', now.strftime('%Y'), now.strftime('%m'), now.strftime('%d'))

os.makedirs(ARTICLE_PATH, exist_ok=True)

with open(os.path.join(ARTICLE_PATH, '{}.rst'.format(title)), 'w') as fp:
    fp.write(article)

if os.path.islink(TODAY_PATH):
    os.remove(TODAY_PATH)
os.symlink(ARTICLE_PATH, TODAY_PATH)


print(PATH)
print(article)
