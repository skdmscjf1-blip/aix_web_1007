
from django.urls import path,include
from . import views

app_name = 'player'

urlpatterns = [
    path('plist/',views.plist,name='plist')
]
