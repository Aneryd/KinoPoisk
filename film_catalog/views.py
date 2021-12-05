from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from film_catalog.kp_parsing import Parsing

def main_view(request):
    film_model = Film.objects.all()
    serial_model = Serial.objects.all()

    if request.POST.get('film_button_list'):
        return render(request, 'index.html', {'film_list': film_model, 'title': 'Главная'})

    if request.POST.get('serial_button_list'):
        return render(request, 'index.html', {'serial_list': serial_model, 'title': 'Главная'})

    if request.POST.get('select_form_status'):
        select_status = request.POST.get('select_form_status')
        serial_id = request.POST.get('id_serial_form')
        film_id = request.POST.get('id_film_form')
        if select_status == 'Избранное':
            status = 1
        elif select_status == 'Просмотренные':
            status = 2
        else:
            status = 3
        if serial_id != None:
            bd_object = Serial.objects.filter(id=serial_id).update(serial_status=status)
        else:
            bd_object = Film.objects.filter(id=film_id).update(film_status=status)

    if request.POST.get('delete_serial_page'):
        serial_id = request.POST.get('id_serial_form')
        if request.POST.get('delete_serial_page') == 'Удалить':
            Serial.objects.filter(id=serial_id).delete()

    if request.POST.get('delete_film_page'):
        film_id = request.POST.get('id_film_form')
        if request.POST.get('delete_film_page') == 'Удалить':
            Film.objects.filter(id=film_id).delete()

    if request.POST.get('add_film_button_page'):
        select_status = request.POST.get('status_film')
        if select_status == 'Избранное':
            status = 1
        elif select_status == 'Просмотренные':
            status = 2
        else:
            status = 3
        film_model1 = Film(film_title=request.POST.get('title_film'), film_status=Status.objects.get(id=status))
        film_model1.save()

    if request.POST.get('add_serial_button_page'):
        select_status = request.POST.get('status_serial')
        if select_status == 'Избранное':
            status = 1
        elif select_status == 'Просмотренные':
            status = 2
        else:
            status = 3
        serial_model1 = Serial(serial_title=request.POST.get('title_serial'), serial_status=Status.objects.get(id=status), series_watch=request.POST.get('series_watching'), series_max=request.POST.get('max_series'))
        serial_model1.save()

    return render(request, 'index.html', {'title': 'Главная'})


def film_view(request):
    film_id_get = request.GET.get('film_id')
    film_id=Film.objects.get(id=film_id_get)
    all_status = Status.objects.all()
    return render(request, 'film_page.html', {'title': film_id.film_title, 'img_film': film_id.film_poster, 'film_name': film_id.film_title, 'film_cat': film_id.film_category,
                                              'film_genre': film_id.film_genre, 'film_desc': film_id.film_description, 'status':film_id.film_status, 'film_id':film_id_get, 'all_status':all_status})

def serial_view(request):
    serial_id_get = request.GET.get('serial_id')
    serial_id=Serial.objects.get(id=serial_id_get)
    all_status = Status.objects.all()

    return render(request, 'serial_page.html', {'title': serial_id.serial_title, 'img_serial': serial_id.serial_poster, 'serial_name': serial_id.serial_title, 'serial_cat': serial_id.serial_category,
                                              'serial_genre': serial_id.serial_genre, 'serial_desc': serial_id.serial_description, 'status': serial_id.serial_status, 'serial_id':serial_id_get, 'all_status':all_status})

def add_film_view(request):
    all_status = Status.objects.all()
    return render(request, 'add_film_page.html', {'title': 'Добавить фильм', 'all_status':all_status})

def add_serial_view(request):
    all_status = Status.objects.all()
    return render(request, 'add_serial_page.html', {'title': 'Добавить сериал', 'all_status':all_status})

def find_parser(request):
    all_status = Status.objects.all()
    return render(request, 'add_film_KinoPoisk.html', {'title': 'Добавить фильм из КП', 'all_status': all_status})

def add_film_KP(request):
    # all_status = Status.objects.all()
    if request.POST.get('KP_add_film'):
        select_status = request.POST.get('status_film_KP')
        if select_status == 'Избранное':
            status = 1
        elif select_status == 'Просмотренные':
            status = 2
        else:
            status = 3

        film_t = Parsing().parse(request.POST.get('KP_title_film'))
        print(film_t[0])
        print(film_t[2])
        for i in film_t[2]:
            print(i)

        for i in Genre.objects.all():
            for j in film_t[2]:
                if j != i:
                    print(j)
                    # model = FilmGenre.objects.get_or_create(genre=Genre.objects.filter(genre_name=j), film=Film.objects.filter(film_title=film_t[0]))
                    model = FilmGenre.objects.get_or_create(genre__genre_name=j, film__film_title=film_t[0])
                    # model.save()

                else:
                    continue

        print(FilmGenre.objects.filter(film=Film.objects.get(film_title=film_t[0])))
        # for i in film_t[2]:
        #     for j in Genre.objects.all():
        #         if j != i:
        #             genre_model = Genre.objects.create(genre_name=i)
        #             genre_model.save()
        #             print(f"i:{i}")
        #             # print(j)
        #         else:
        #             continue
        #         print(f"j:{j}")
        # for i in film_t[2]:
            # genre_model = Genre.objects.get_or_create(genre_name=str(i))
            # genre_model.save()
            # film_model = Film(film_title=film_t[0], film_status=Status.objects.get(id=status), film_genre=Genre.objects.get_or_create(genre_name=i))
            # film_model.save()
            # print(Genre.objects.all())
        # film_model = Film(film_title=film_t[0], film_status=Status.objects.get(id=status))
        # film_model.save()
        
    return render(request, 'index.html', {'title': 'Главная'})
