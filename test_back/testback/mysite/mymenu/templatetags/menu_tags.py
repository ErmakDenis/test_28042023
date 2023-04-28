from django import template
from django.urls import resolve, reverse
from django.utils.safestring import mark_safe
from django.utils.html import escape

from mymenu.models import Category  # здесь app - имя вашего приложения

register = template.Library()

@register.simple_tag(takes_context=True)
def menu(context):
    current_url = resolve(context['request'].path_info).url_name
    categories = Category.objects.all().order_by('name')
    html = build_menu(categories, current_url)
    return mark_safe(html)


def build_menu(categories, current_url):
    html = '<ul>'
    for category in categories:
        if category.parent is None:
            # if current_url == category.slug:
            #     name = str(category.name).upper()
            # else:
            #     name = category.name
            html +='<li>' + f'<a href="#">{category.name}</a>'
            html += build_sub_menu(category, current_url)
            html +='</li>'
    html += '</ul>'
    return html


def build_sub_menu(category, current_url):
    sub_categories = category.children.all().order_by('name')
    if not sub_categories:
        return ''

    html = '<ul>'
    for sub_category in sub_categories:
        # if current_url == sub_category.slug:
        #     name = str(sub_category.name).upper()
        # else:
        #     name = sub_category.name
        html += '<li>' + f'<a href="#">{sub_category.name}</a>'
        html += build_sub_menu(sub_category, current_url)
        html += '</li>'
    html += '</ul>'
    return html
