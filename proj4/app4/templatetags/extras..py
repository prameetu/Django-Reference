from django import template

register = template.Library()

def cut(val,arg):
    #This cut out all value of arg in val

    return val.replace(arg,'')


register.filter('cut',cut)