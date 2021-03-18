#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Adrian'
SITENAME = 'Past Climate'
SITEURL = 'https://adrian-95.github.io'
SITETITLE = "Adrian Popescu"
SITESUBTITLE = " Geoscientist | Python Developer | Writer " 
SITEDESCRIPTION = "Past Climate"
SITELOGO = "https://adrian-95.github.io/images/profile.png"
THEME = 'Flex'
STATIC_PATHS = ['images', 'static']
FAVICON = "https://adrian-95.github.io/images/favicon.png"
CUSTOM_CSS = 'static/custom.css'

COPYRIGHT_YEAR = 2020
BROWSER_COLOR = "#333"
ROBOTS = "index, follow"
PYGMENTS_STYLE = "borland"

MAIN_MENU = True
DISABLE_URL_HASH = True
MENUITEMS = (
    ("Index", "/index.html"),
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Projects', 'https://github.com/Adrian-95'),
    ('Ancient Earth', 'https://dinosaurpictures.org/ancient-earth?fbclid=IwAR3Bgt214CTVFTYiY8OfVBXHDakF-Oe_pYm53V48ssibVii5XnVVldwtBjE#90')
)

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/adrian-popescu-59b502142/'),
    ('github', 'https://github.com/Adrian-95'),
    ('twitter', 'https://twitter.com/past_climate'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True