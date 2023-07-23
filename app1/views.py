from django.shortcuts import render

# Create your views here.
def sim(request):
    return render(request,'render.html')