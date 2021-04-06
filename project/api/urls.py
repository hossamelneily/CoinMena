from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    re_path(r'^v1/', include('project.api.v1.urls')),
]
