#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'cocuh'
SITENAME = "cocuh's blog"
SITETITLE = "cocuh"
SITESUBTITLE = "Kosuke Kusano"
SITEURL = ''

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index-{lang}.html'

PATH = 'content'
STATIC_PATHS = ['static', '']

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = [
    'summary',
    'sitemap',
    'share_post',
    'render_math',
]
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    },
}

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

ROBOTS = 'index, follow'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('home', 'http://typowriter.org'),
        ('category', '/categories.html'),
        ('tag', '/tags.html'),
)

# Social widget
SOCIAL = (
        ('linkedin', 'https://www.linkedin.com/in/kosukekusano'),
        ('github', 'https://github.com/cocuh'),
        ('google', 'https://plus.google.com/118080418876092260093'),
        ('twitter', 'https://twitter.com/cocuh_'),
        ('rss', '/feeds/all.atom.xml'),
)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme/Flex'
SITELOGO = '/static/sitelogo.png'
PYGMENTS_STYLE = 'monokai'
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
