from __future__ import unicode_literals

from django.conf import settings


MARKDOWNY = {
    'output_format': 'html5',
    'lazy_ol': False,
}

markdowny_user = getattr(settings, 'MARKDOWNY', {})

MARKDOWNY.update(markdowny_user)
