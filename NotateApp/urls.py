from typing import Text
from django.conf.urls import url
from NotateApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^test/$',views.Txtapi),
    url(r'^test/([0-9]+)$',views.Txtapi) ]