from django.urls import path

# Al poner from . quiere decir, de este directorio
from . import views
urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:nombrePersona>", views.bienvenida, name = "bienvenida"),
    path("victor", views.victor, name = "victor"),
    path("brian", views.brian, name = "brian")
]