from __future__ import unicode_literals

from django.template import Context, Template
from django.test import TestCase


class MarkdownyTestCase(TestCase):
    """Markdowny test cases."""

    def test_markdowny(self):
        out = Template(
            "{% load markdowny_tags %}"
            "{% markdowny %}"
            '# Hello, world!'
            "{% endmarkdowny %}"
        ).render(Context())
        self.assertEqual(out, '<h1>Hello, world!</h1>')
