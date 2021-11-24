from django import template
from django.template.base import FilterExpression
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from markdown import markdown

from ..utils.markdowny import parse_tag
from .. import settings

register = template.Library()


@register.filter(name="markdowny", is_safe=True)
@stringfilter
def markdowny_filter(value):
    return mark_safe(markdown(value, **settings.MARKDOWNY))


class MarkdownyNode(template.Node):
    def __init__(self, nodelist, kwargs):
        self.nodelist = nodelist
        self.kwargs = kwargs

    def render(self, context):
        output = self.nodelist.render(context)
        for key in self.kwargs:
            if isinstance(self.kwargs[key], FilterExpression):
                try:
                    self.kwargs[key] = self.kwargs[key].resolve(context)
                except template.VariableDoesNotExist:
                    self.kwargs[key] = settings.MARKDOWNY[key]
        return mark_safe(markdown(output, **self.kwargs))


@register.tag(name="markdowny")
def markdowny_tag(parser, token):
    # Parse tag contents
    tag_name, args, kwargs = parse_tag(parser, token)

    # Update settings with tag keyword arguments
    options = settings.MARKDOWNY.copy()
    options.update(kwargs)

    nodelist = parser.parse(("endmarkdowny",))
    parser.delete_first_token()
    return MarkdownyNode(nodelist, options)
