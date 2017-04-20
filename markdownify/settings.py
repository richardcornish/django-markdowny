from __future__ import unicode_literals

from django.conf import settings


MARKDOWNIFY = {
    'output_format': 'html5',
    'lazy_ol': False,
}

markdownify_user = getattr(settings, 'MARKDOWNIFY', {})

MARKDOWNIFY.update(markdownify_user)
