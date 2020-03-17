import datetime

from django import template

register = template.Library()


@register.filter()
def bizzfuzz(value):
    value = int(value)
    if value % 15 == 0:
        return "FizzBuzz"
    elif value % 3 == 0:
        return "Fizz"
    elif value % 5 == 0:
        return "Buzz"
    else:
        return value


@register.filter()
def age(bday, today=datetime.date.today()):
    result = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
    if result > 13:
        return "allowed"
    else:
        return "blocked"
