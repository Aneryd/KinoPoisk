from django.urls import path

from .views import main_view, film_view, serial_view, add_film_view, add_serial_view, find_parser, add_film_KP

# from .views import Main

urlpatterns = [
    path('', main_view, name='main'),
    path(r'film', film_view, name='film_view'),
    path(r'serial', serial_view, name='serial_view'),
    path(r'add_film', add_film_view, name='add_film'),
    path(r'add_serial', add_serial_view, name='add_serial'),
    path(r'KP_parse', find_parser, name="find_parser"),
    path(r'add_kp', add_film_KP, name='add_film_KP')
]
