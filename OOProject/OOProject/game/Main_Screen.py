from .user import *
from django import template

register = template.Library()


@register.simple_tag
class MainScreen:

    @register.filter
    def newGame(self):
        print("making new userinstance")
        user = User.getInstance()



