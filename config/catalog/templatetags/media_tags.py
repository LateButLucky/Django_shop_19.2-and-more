from django import template

register = template.Library()


@register.filter(name='mymedia')
def mymedia(path):
    if path:
        return f'/media/{path}'
    return '#'
