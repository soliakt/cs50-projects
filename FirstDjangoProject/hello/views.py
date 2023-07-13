from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# El request que toma como argumento es la solicitud HTTP que el usuario
# ha hecho para acceder a nuestra aplicación
def index(request):
    # return HttpResponse("Hello! Django here hehe")
    return render(request, "hello/index.html")

def victor(request):
    return HttpResponse("Hello to you too, Víctor!")


def brian(request):
    return HttpResponse("It looks like you're not Victor, I guess you're, Brian?")

def bienvenida(request, nombrePersona):
    # return HttpResponse(f"Hello, {nombrePersona.capitalize()}!")
    return render(request, "hello/greet.html", {
        "nombrePersona": nombrePersona.capitalize()
    })