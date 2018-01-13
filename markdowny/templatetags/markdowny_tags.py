from __future__ import unicode_literals

from django import template
from django.utils.safestring import mark_safe

from ..utils.markdowny import bits_to_dict, markdown as _markdown
from .. import settings

register = template.Library()


@register.filter(name='markdowny')
def markdowny_filter(value):
    return mark_safe(_markdown(value, options=settings.MARKDOWNY))


class MarkdownyNode(template.Node):
    def __init__(self, nodelist, **kwargs):
        self.nodelist = nodelist
        self.options = kwargs['options']

    def render(self, context):
        output = self.nodelist.render(context)
        return _markdown(output, options=self.options)


@register.tag(name='markdowny')
def markdowny_tag(parser, token):

    # Convert tag kwargs to dictionary
    bits = token.split_contents()
    remaining_bits = bits[1:]
    tag_options = bits_to_dict(remaining_bits)

    # Update settings with tag options
    options = settings.MARKDOWNY.copy()
    options.update(tag_options)

    nodelist = parser.parse(('endmarkdowny',))
    parser.delete_first_token()
    return MarkdownyNode(nodelist, options=options)
