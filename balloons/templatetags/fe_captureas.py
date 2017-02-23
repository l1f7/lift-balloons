# -*- coding: utf-8 -*-
"""Template tags."""

from django import template

register = template.Library()


@register.tag(name='captureas')
def do_captureas(parser, token):
    """Capture a block's content for re-use throughout a template.
    particularly handy for use within social meta fields that are virtually
    identical. See templates/base/base.html or templates/wagtail/base.html for
    implementation details/examples.
    """
    try:
        tag_name, args = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError('Requires a variable name.')
    nodelist = parser.parse(('endcaptureas',))
    parser.delete_first_token()
    return CaptureasNode(nodelist, args)


class CaptureasNode(template.Node):
    """Container class."""

    def __init__(self, nodelist, varname):
        """Initialize class."""
        self.nodelist = nodelist
        self.varname = varname

    def render(self, context):
        """Render the data."""
        output = self.nodelist.render(context)
        context[self.varname] = output
        return ''
