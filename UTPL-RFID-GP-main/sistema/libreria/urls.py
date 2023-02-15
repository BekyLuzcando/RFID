from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('prueba', views.prueba, name='prueba'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('libros/editar/<int:id>', views.editar, name='editar'),
    path('programa', views.programa, name='programa'),
    path('anaqueltry', views.anaqueltry, name='anaqueltry'),
    path('timer', views.timer, name='timer')

]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)