from django.contrib import admin
from django.urls import path

from dodoTA.views import test, testinput, show_shalgham, form2

urlpatterns = [
    path('ad/', test ),
    path('de/', testinput ),
    path('booshbaba/', show_shalgham ),
    path('b/', form2, name="uname"),
]