from django.urls import path
from .views import *

urlpatterns=[
    path(' ', display_all),
    path('/ /<str:title>', display_blog),
    path('/create', create),
    path('/edit', edit)
]