from django.urls import path
from .views import *
from .requests_to_api import *


urlpatterns = [
    path('/search', view_response, name='view_response_url')
]
