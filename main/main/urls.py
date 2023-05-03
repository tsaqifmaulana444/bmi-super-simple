from django.contrib import admin
from django.urls import path
from bmiapps.views import home, track

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('track/', track, name='track')
]
