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