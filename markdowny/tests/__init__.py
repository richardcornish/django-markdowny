from django.template import Context, Template
from django.test import TestCase, override_settings

from .. import settings


class MarkdownyTestCase(TestCase):
    """Markdowny test cases."""

    def test_filter_p(self):
        out = Template(
            "{% load markdowny_tags %}" "{{ 'Hello, world!'|markdowny }}"
        ).render(Context())
        self.assertEqual(out, "<p>Hello, world!</p>")

    def test_filter_h1(self):
        out = Template(
            "{% load markdowny_tags %}" "{{ '#Hello, world!'|markdowny }}"
        ).render(Context())
        self.assertEqual(out, "<h1>Hello, world!</h1>")

    def test_tag_p(self):
        out = Template(
            "{% load markdowny_tags %}"
            "{% markdowny %}"
            "Hello, world!"
            "{% endmarkdowny %}"
        ).render(Context())
        self.assertEqual(out, "<p>Hello, world!</p>")

    def test_tag_h1(self):
        out = Template(
            "{% load markdowny_tags %}"
            "{% markdowny %}"
            "# Hello, world!"
            "{% endmarkdowny %}"
        ).render(Context())
        self.assertEqual(out, "<h1>Hello, world!</h1>")

    def test_tag_tab_length(self):
        out = Template(
            "{% load markdowny_tags %}"
            "{% markdowny %}"
            "\t\tHello, world!"
            "{% endmarkdowny %}"
        ).render(Context())
        self.assertEqual(out, "<pre><code>    Hello, world!\n</code></pre>")

    def test_tag_tab_length_2(self):
        out = Template(
            "{% load markdowny_tags %}"
            "{% markdowny tab_length=2 %}"
            "\t\tHello, world!"
            "{% endmarkdowny %}"
        ).render(Context())
        self.assertEqual(out, "<pre><code>  Hello, world!\n</code></pre>")

    def test_tag_output_format(self):
        out = Template(
            "{% load markdowny_tags %}"
            "{% markdowny %}"
            "Hello,  \nworld!"
            "{% endmarkdowny %}"
        ).render(Context())
        self.assertEqual(out, "<p>Hello,<br>\nworld!</p>")

    def test_tag_output_format_html(self):
        out = Template(
            "{% load markdowny_tags %}"
            "{% markdowny output_format='html' %}"
            "Hello,  \nworld!"
            "{% endmarkdowny %}"
        ).render(Context())
        self.assertEqual(out, "<p>Hello,<br>\nworld!</p>")

    def test_tag_output_format_xhtml(self):
        out = Template(
            "{% load markdowny_tags %}"
            "{% markdowny output_format='xhtml' %}"
            "Hello,  \nworld!"
            "{% endmarkdowny %}"
        ).render(Context())
        self.assertEqual(out, "<p>Hello,<br />\nworld!</p>")

    def test_tag_extensions(self):
        out = Template(
            "{% load markdowny_tags %}"
            "{% markdowny extensions=extensions %}"
            "HTML\n*[HTML]: HyperText Markup Language"
            "{% endmarkdowny %}"
        ).render(
            Context(
                {
                    "extensions": ["abbr"],
                }
            )
        )
        self.assertEqual(
            out, '<p><abbr title="HyperText Markup Language">HTML</abbr></p>'
        )

    def test_tag_kwarg_fallback(self):
        out = Template(
            "{% load markdowny_tags %}"
            "{% markdowny extensions=extensions %}"
            "HTML\n*[HTML]: HyperText Markup Language"
            "{% endmarkdowny %}"
        ).render(Context())
        self.assertEqual(out, "<p>HTML\n*[HTML]: HyperText Markup Language</p>")

    def test_tag_extension_configs(self):
        out = Template(
            "{% load markdowny_tags %}"
            "{% markdowny extensions=extensions extension_configs=extension_configs %}"
            "Hello, world![^1]\n[^1]: Or wherever."
            "{% endmarkdowny %}"
        ).render(
            Context(
                {
                    "extensions": ["footnotes"],
                    "extension_configs": {
                        "footnotes": {
                            "SEPARATOR": ":",
                        },
                    },
                }
            )
        )
        self.assertEqual(
            out,
            '<p>Hello, world!<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></p>\n'
            '<div class="footnote">\n'
            "<hr>\n"
            "<ol>\n"
            '<li id="fn:1">\n'
            '<p>Or wherever.&#160;<a class="footnote-backref" href="#fnref:1" title="Jump back to footnote 1 in the text">&#8617;</a></p>\n'
            "</li>\n"
            "</ol>\n"
            "</div>",
        )

    def test_tag_settings_override(self):
        settings.MARKDOWNY["output_format"] = "xhtml"
        with override_settings(MARKDOWNY=settings.MARKDOWNY):
            out = Template(
                "{% load markdowny_tags %}"
                "{% markdowny %}"
                "Hello,  \nworld!"
                "{% endmarkdowny %}"
            ).render(Context())
            self.assertEqual(out, "<p>Hello,<br />\nworld!</p>")

    def test_tag_settings_override_override(self):
        settings.MARKDOWNY["output_format"] = "xhtml"
        with override_settings(MARKDOWNY=settings.MARKDOWNY):
            out = Template(
                "{% load markdowny_tags %}"
                "{% markdowny output_format='html' %}"
                "Hello,  \nworld!"
                "{% endmarkdowny %}"
            ).render(Context())
            self.assertEqual(out, "<p>Hello,<br>\nworld!</p>")
