# -*- coding: utf-8 -*-
"""Custom template filters.

This file would be used to add any custom filters that are created for a
project. Not likely to be used very often, but it seemed to make sense to
maintain filters as an actual library for our reference moving forward.
"""
from django import template

register = template.Library()


@register.filter
def to_class_name(value):
    """Convert the current view's object to a usable class name.

    Useful for outputting a css-class for targetting specific styles or
    javascript functionality on a per-view basis, for example:

    <div class="siteContainer {% if request.path == '/' %}home{% else %}{{ object|to_class_name|lower }}{% endif %}">  # noqa

    """
    return value.__class__.__name__


@register.filter(name='removeEmptyPs')
def remove_empty_ptags(string):
    """Remove empty paragraph tags.

    In certain CMS systems, every line-break gets automatically converted
    into new paragraph tags, which means people coming from Word-like
    writing programs can cause serious layout issues. This allows you
    to strip out any empty B.S. that shouldn't be there in fields that
    are supposed to be rendered with html (and/or richtext)

    {{ self.side_content|removeEmptyPs|richtext }}

    """
    return (string
            .replace('<p></p>', '')
            .replace('<p><br></p>', '')
            .replace('<p><br/></p>', ''))
