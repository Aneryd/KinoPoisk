from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=255, verbose_name="Имя пользователя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия пользователя")
    login = models.CharField(max_length=100, verbose_name="Логин пользователя")
    password = models.CharField(max_length=100, verbose_name="Пароль пользователя")

    def __str__(self):
        return self.first_name


class Category(models.Model):

    category_name = models.CharField(max_length=255, verbose_name="Название категории")

    def __str__(self):
        return self.category_name


class Genre(models.Model):

    genre_name = models.CharField(max_length=255, verbose_name="Название жанра")

    def __str__(self):
        return self.genre_name


class Status(models.Model):

    status_name = models.CharField(default=None, max_length=255, verbose_name="Название статуса")

    def __str__(self):
        return self.status_name


class Film(models.Model):

    film_title = models.CharField(max_length=255, verbose_name='Название фильма')
    film_category = models.ForeignKey(Category, verbose_name="Категория фильма", on_delete=models.CASCADE, blank=True, null=True)
    film_genre = models.ForeignKey(Genre, verbose_name="Жанр фильма", on_delete=models.CASCADE, blank=True, null=True)
    film_status = models.ForeignKey(Status, verbose_name="Статус фильма", on_delete=models.CASCADE, null=True)
    film_poster = models.ImageField(verbose_name="Постер к фильму", blank=True, null=True)
    film_description = models.TextField(verbose_name="Описание к фильму", blank=True, null=True)

    def __str__(self):
        return self.film_title


class Serial(models.Model):

    serial_title = models.CharField(max_length=255, verbose_name="Название сериала")
    serial_category = models.ForeignKey(Category, verbose_name="Категория сериала", on_delete=models.CASCADE, blank=True, null=True)
    serial_genre = models.ForeignKey(Genre, verbose_name="Жанр сериала", on_delete=models.CASCADE, blank=True, null=True)
    serial_status = models.ForeignKey(Status, verbose_name="Статус сериала", on_delete=models.CASCADE, null=True, blank=True)
    serial_poster = models.ImageField(verbose_name="Постер к сериалу", blank=True, null=True)
    serial_description = models.TextField(verbose_name="Описание к сериалу", null=True, blank=True)
    series_watch = models.IntegerField(default=0, verbose_name="Просмотренные серии", blank=True)
    series_max = models.IntegerField(verbose_name="Максимальное количество серий", blank=True)

    def __str__(self):
        return self.serial_title


class FilmCategory(models.Model):

    film = models.ForeignKey(Film, verbose_name="Фильм", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.CASCADE)


class SerialCategory(models.Model):

    serial = models.ForeignKey(Serial, verbose_name="Сериал", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.CASCADE)


class FilmGenre(models.Model):

    film = models.ForeignKey(Film, verbose_name="Фильм", on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, verbose_name="Жанры", on_delete=models.CASCADE)


class SerialGenre(models.Model):

    serial = models.ForeignKey(Serial, verbose_name="Сериал", on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, verbose_name="Жанры", on_delete=models.CASCADE)


class FilmUser(models.Model):

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    film = models.ForeignKey(Film, verbose_name="Фильм", on_delete=models.CASCADE)


class SerialUser(models.Model):

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    serial = models.ForeignKey(Serial, verbose_name="Сериал", on_delete=models.CASCADE)