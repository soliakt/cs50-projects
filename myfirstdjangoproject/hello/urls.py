# El proyecto tiene su propio urls, pero 
# interesa tener dentro de la app tambien un urls
from django.urls import path

from . import views
#From . significa desde este directorio...


urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:name>", views.greet, name="greet"),
    path("brian", views.brian, name = "brian"),
    path("david", views.david, name = "david")
]
