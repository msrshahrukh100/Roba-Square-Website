from django import template
from authentication.username import get_user_name



register = template.Library()



@register.filter(name='addclass')
def addclass(field,css) :
	return field.as_widget(attrs={"class":css})


@register.filter(name='addtype')
def addtype(field,css) :
	return field.as_widget(attrs={"type":css})


@register.filter(name='times') 
def times(number):
    return range(number)

@register.filter(name="getfullname")
def getfullname(user) :
	return get_user_name(user)


@register.filter(name="list")
def list(number) :
	return [i for i in range(1,number+1)]

@register.filter(name="subtractfromfive")
def subtractfromfive(number) :
	return 5 - int(number)
