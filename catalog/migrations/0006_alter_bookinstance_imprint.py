# Generated by Django 4.1.3 on 2022-11-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_rename_genre_book_genres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='imprint',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]