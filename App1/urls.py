from django.urls import path 
from .views import home_view, playstation , monitor , joystick , keybord 

urlpatterns =[
    path ("",home_view, name="home"),
    path('playstation/', playstation, name='playstation'),
    path('monitor/', monitor, name='monitor'),
    path('joystick/', joystick, name='joystick'),
    path('keybord/', keybord, name='keybord'),
]