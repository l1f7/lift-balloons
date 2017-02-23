# -*- coding: utf-8 -*-
"""Template tags for manipulating form elements."""
from django import template

register = template.Library()


@register.filter(name='checkFormClass')
def check_form_class(field):
    """Return the form element type for comparison in templates.

    Example:
        {% if field|checkFormClass == 'SelectMultiple' %}

    You can {{ field|checkFormClass }} if you want to see the
    various values that your form fields are registered as
    """
    return field.field.widget.__class__.__name__


@register.filter(name='add_css')
def add_css(field, css):
    """Add css to form field.

    Example:
        {{ field|add_css:"chosen-select" }}
    """
    return field.as_widget(attrs={'class': css})


@register.filter(name='add_required')
def add_required(field):
    """Add required to a field.

    Example:
        {% if field.field.required %}
          {{ field|add_required }}
        {% endif %}
    """
    return field.as_widget(
            attrs={'aria-required': 'true', 'required': 'required'})


@register.filter(name='add_attr')
def add_attr(field, values):
    """Add attribute to an element.

    Example:
        {{ field|add_attr:'placeholder="Sample Text"'' }}
    """
    return field.as_widget(attrs=values)
