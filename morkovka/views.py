from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def end(request):
    return render(request, "finish.html")
