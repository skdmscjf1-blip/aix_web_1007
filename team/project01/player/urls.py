
from django.urls import path,include
from . import views

app_name = 'player'

urlpatterns = [
    path('plist/',views.plist,name='plist'),
    path('pview/<int:id>/',views.pview,name='pview'),
]
