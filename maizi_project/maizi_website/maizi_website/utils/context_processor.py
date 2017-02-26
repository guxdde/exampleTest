#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016/3/7
@author: guxdde
utils模块context_proecssor业务处理。
"""

from maizi_website import settings


def maizi(request):
    return {'site_name': settings.SITE_NAME,
            'meta_keywords': settings.META_KEYWORDS,
            'meta_description': settings.META_DESCRIPTION,
            'request': request}
