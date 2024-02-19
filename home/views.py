from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return HttpResponse("this is a aboutpage ")

def services(request):
    return HttpResponse("this is a servicepage")


def contacts(request):
    return HttpResponse("this is a contacts")