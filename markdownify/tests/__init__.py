from __future__ import unicode_literals

from django.template import Context, Template
from django.test import TestCase


class MarkdownifyTestCase(TestCase):
    """Markdownify test cases."""

    def test_markdownify(self):
        out = Template(
            "{% load markdownify_tags %}"
            "{% markdownify %}"
            '# Hello, world!'
            "{% endmarkdownify %}"
        ).render(Context())
        self.assertEqual(out, '<h1>Hello, world!</h1>')
