from django.urls import path
from .views import *
from .requests_to_api import *


urlpatterns = [
    path('', view_response)
]
