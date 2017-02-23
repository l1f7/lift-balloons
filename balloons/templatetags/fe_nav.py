# -*- coding: utf-8 -*-
"""Templat tags for navigation."""
import re

from django import template
from django.core.urlresolvers import reverse_lazy

register = template.Library()


@register.simple_tag
def active_nav(request, pattern):
    """Output 'is-active' class for html tags.

    Outputs `is-active` when the website slug (exclusive of /'s)
    matches the submitted pattern, for example:
      <a href="/contact" class="{% active_nav request "contact" %}">Contact</a>

    The above would render, if the user is on the `/contact/` page, as:
      <a href="/contact/" class="is-active">Contact</a>

    This is useful for basic pages that are unlikely to change. However,
    if you are using url looksup (`<a href="{% url 'feed' %}">`), then
    you should use the `reverse_active_nav` tag below.
    """
    if re.search('^/%s/' % (pattern,), request.path):
        return 'is-active'
    elif request.path == '/':
        return 'is-home'
    return ''


@register.simple_tag
def reverse_active_nav(request, pattern, url_name, *args, **kwargs):
    """Output 'is_active' using reverse url lookups.

    Outputs `is-active` when the reverse `url` looks matches the submitted
    pattern, for example:
      <a href="{% url 'feed' %}" class="{% reverse_active_nav request url "feed" %} w-ActionNav__link">Explore Topics</a>  # noqa

    The above would render, if the user is on the `/contact/` page, as:
      <a href="/contact/" class="is-active">Contact</a>
    """
    url = reverse_lazy(url_name, args=args)
    if re.search('^/%s/' % (pattern,), str(url)):
        return 'is-active'

    return ''


@register.simple_tag
def url_replace(request, field, value):
    """URL Replace.

    Allows us to quickly and easily swap parameters in the request
    object in the case of doing complex queries like filtering
    a certain search results, feed, or metadata. Pour exemple:
      <a href="?{% url_replace request 'viewing' 'unanswered' %}" class="feedNav-link">Unanswered</a> # noqa

    And let's pretend the url currently looks like this:
      http://app.dev/feed/?viewing=all&topic=Chronic%20Pain

    Clicking on that link would generate a URL like this:
      http://app.dev/feed/?viewing=unaswered&topic=Chronic%20Pain
    """
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
