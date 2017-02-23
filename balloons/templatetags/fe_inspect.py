# -*- coding: utf-8 -*-
"""Library for inspecting variables and objects that are within your views."""
from django.template import Library

register = Library()


@register.simple_tag
def template_dir(this_object):
    """Template_dir dumps all of the methods and properties of an object.

    Example:
        {% template_dir blog_post %}
    """
    output = dir(this_object)
    return '<code>%s</code>' % str(output)


@register.simple_tag
def template_dict(this_object):
    """Dump all of the properties for an object/variable.

    This is generally more useful for frontend than template_dir because we
    normally don't need access to the objects method's on the frontend and
    makes the dump much smaller/quicker to scan through to find what you need

    Example:
        {% template_didct blog_post %}
    """
    output = this_object.__dict__
    return '<code>%s</code>' % str(output)


@register.simple_tag
def template_meta(this_object):
    """Dump object's meta."""
    meta = dir(this_object._meta)
    return '<code>%s</code>' % str(meta)


@register.simple_tag
def template_class(this_object):
    """Dump the object's class."""
    cls = this_object.__class__
    return '<code>%s</code>' % str(cls)


@register.simple_tag
def template_repr(this_object):
    """Dump the representation of the object."""
    output = this_object.__repr__
    return '<code>%s</code>' % str(output)
