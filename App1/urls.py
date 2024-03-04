from django.urls import path 
from .views import home_view, playstation , monitor , joystick , keybord , monitorpage , monitor1 , monitor2 , monitor3
from .views import joystickpage , joystick1 , joystick2 , joystick3

urlpatterns =[
    path ("",home_view, name="home"),
    path('playstation/', playstation, name='playstation'),
    path('monitor/', monitor, name='monitor'),
    path('joystick/', joystick, name='joystick'),
    path('keybord/', keybord, name='keybord'),
    path('monitorpage/', monitorpage, name='monitorpage'),
    path('monitor1/', monitor1, name='monitor1'),
    path('monitor2/', monitor2, name='monitor2'),
    path('monitor3/', monitor3, name='monitor3'),
    path('joystickpage/', joystickpage, name='joystickpage'),
    path('joystick1/', joystick1, name='joystick1'),
    path('joystick2/', joystick2, name='joystick2'),
    path('joystick3/', joystick3, name='joystick3'),
]