from django.template.defaulttags import register

""" В шаблонизаторе джанги нельзя сделать обращение по типу
    obj[other_obj['value']], сделан фильтр кастомный,
    применяется через | {{ shop_dict|get_item:obj_deal.storeID }}
"""


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def url(string, arg):
    return string.replace(arg, '')
