# Generated by Django 4.2 on 2023-04-28 20:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='название')),
                ('title', models.CharField(blank=True, max_length=30, verbose_name='заглавие')),
                ('author', models.CharField(max_length=30, verbose_name='автор')),
                ('description', models.TextField(blank=True, max_length=512, verbose_name='описание')),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)], verbose_name='цена')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=12, verbose_name='имя столбца')),
                ('is_visible', models.BooleanField(verbose_name='видимый')),
            ],
        ),
    ]
