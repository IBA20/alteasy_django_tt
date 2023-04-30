from django.db import models
from django.core.validators import MaxValueValidator


class Book(models.Model):
    name = models.CharField(
        'название',
        max_length=20
    )
    title = models.CharField(
        'заглавие',
        max_length=30,
        blank=True,
    )
    author = models.CharField(
        'автор',
        max_length=30,
    )
    description = models.TextField(
        'описание',
        max_length=512,
        blank=True,
    )
    price = models.PositiveIntegerField(
        'цена',
        validators=[MaxValueValidator(99999)],
    )

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return f'{self.author} {self.name}'


class Profile(models.Model):
    column_name = models.CharField(
        'имя столбца',
        max_length=12
    )
    is_visible = models.BooleanField(
        'видимый'
    )

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def __str__(self):
        return f'{self.column_name} {self.is_visible}'
