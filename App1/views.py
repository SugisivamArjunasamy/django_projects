from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'index.html')
def playstation(request):
    return render(request, 'playstation.html')
def monitor(request):
    return render(request, 'monitor.html')
def joystick(request):
    return render(request, 'joystick.html')
def keybord(request):
    return render(request, 'keybord.html')
def monitorpage(request):
    return render(request, 'monitorpage.html')
def monitor1(request):
    return render(request, 'monitor1.html')
def monitor2(request):
    return render(request, 'monitor2.html')
def monitor3(request):
    return render(request, 'monitor3.html')
def joystickpage(request):
    return render(request, 'joystickpage.html')
def joystick1(request):
    return render(request, 'joystick1.html')
def joystick2(request):
    return render(request, 'joystick2.html')
def joystick3(request):
    return render(request, 'joystick3.html')