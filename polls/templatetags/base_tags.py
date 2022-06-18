from django import template

from polls.models import Category, Tag, Content


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_tags():
    return Tag.objects.all()


@register.inclusion_tag('tags/get_last.html')
def get_last_content(items=3):
    last_content = Content.objects.order_by('id')[:items]
    return {'last_content': last_content}
