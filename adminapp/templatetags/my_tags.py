from django import template
from django.conf import settings

register = template.Library()


@register.filter(name="media_folder_products")
def media_folder_products(string):
    if not string:
        string = "products_images/default.jpg"
    return f"{settings.MEDIA_URL}{string}"


def media_folder_users(string):
    if not string:
        string = "users_avatar/default.jpg"
    return f"{settings.MEDIA_URL}{string}"


@register.filter(name="css_folder")
def css_folder(string):
    if not string:
        string = "css/st.css"
    return f"{settings.STATIC_URL}{string}"


register.filter("media_folder_users", media_folder_users)
