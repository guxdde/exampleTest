# -*- coding: utf-8 -*-

from shopsys import settings
from shopsys.apps.catalog.models import Category


def shopsys(request):
    return {
        'active_categories': Category.object.filter(is_active=True),
        'site_name': settings.SITE_NAME,
        'meta_keywords': settings.META_KEYWORDS,
        'meta_description': settings.META_DESCRIPTION,
        'request': request
    }
