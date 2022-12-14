# Generated by Django 4.1 on 2022-09-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarangWatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField()),
                ('title', models.TextField()),
                ('rating', models.IntegerField()),
                ('release_date', models.TextField()),
                ('review', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='MyWatchList',
        ),
    ]
