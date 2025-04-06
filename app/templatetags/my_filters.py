from django import template

register = template.Library()

@register.filter
def format_price(value):
    # 1,234,567.00 to 1 234 567
    return f"{round(value):,}".replace(",", " ")
