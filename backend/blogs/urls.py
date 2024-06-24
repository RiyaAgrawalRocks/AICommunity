from django.urls import path
from .views import *

urlpatterns=[
    path('', display_all),
    path('<int:id>/', display_blog),
    path('member/', display_members)
]