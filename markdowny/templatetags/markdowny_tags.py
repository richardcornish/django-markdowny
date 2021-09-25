from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import escape
from django.utils.safestring import mark_safe

from ..utils.markdowny import markdown as _markdown
from .. import settings

register = template.Library()


@register.filter(name="markdowny", is_safe=True, needs_autoescape=True)
@stringfilter
def markdowny_filter(value, autoescape=True):
    value = escape(value) if autoescape else value
    return mark_safe(_markdown(value, **settings.MARKDOWNY))


class MarkdownyNode(template.Node):
    def __init__(self, nodelist, options):
        self.nodelist = nodelist
        self.options = options

    def render(self, context):
        output = self.nodelist.render(context)
        for key in self.options:
            if isinstance(self.options[key], template.Variable):
                try:
                    self.options[key] = self.options[key].resolve(context)
                except template.VariableDoesNotExist:
                    self.options[key] = settings.MARKDOWNY[key]
        return mark_safe(_markdown(output, **self.options))


@register.tag(name="markdowny")
def markdowny_tag(parser, token):
    bits = token.split_contents()[1:]

    # Create dictionary from tag keyword arguments
    tag_options = {bit.split("=")[0]: bit.split("=")[1] for bit in bits}

    # Coerce arguments because token.split_contents() unpacks string literals
    for key in tag_options:
        s = tag_options[key]
        if (s[0] == s[-1]) and s.startswith(("'", '"')):
            tag_options[key] = s[1:-1]
        else:
            try:
                tag_options[key] = int(s)
            except ValueError:
                tag_options[key] = template.Variable(s)

    # Update settings options with tag options
    options = settings.MARKDOWNY.copy()
    options.update(tag_options)

    nodelist = parser.parse(("endmarkdowny",))
    parser.delete_first_token()
    return MarkdownyNode(nodelist, options)
