from __future__ import unicode_literals

from django import template

from ..utils.markdownify import bits_to_dict, markdownify as _markdownify
from .. import settings

register = template.Library()


class MarkdownifyNode(template.Node):
    def __init__(self, nodelist, **kwargs):
        self.nodelist = nodelist
        self.options = kwargs['options']

    def render(self, context):
        output = self.nodelist.render(context)
        return _markdownify(output, options=self.options)


@register.tag
def markdownify(parser, token):

    # Convert tag kwargs to dictionary
    bits = token.split_contents()
    remaining_bits = bits[1:]
    tag_options = bits_to_dict(remaining_bits)

    # Update settings with tag options
    options = settings.MARKDOWNIFY.copy()
    options.update(tag_options)

    nodelist = parser.parse(('endmarkdownify',))
    parser.delete_first_token()
    return MarkdownifyNode(nodelist, options=options)
