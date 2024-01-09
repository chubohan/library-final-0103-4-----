# Generated by Django 4.2.6 on 2024-01-02 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='不願意透漏身份的人', max_length=10)),
                ('message', models.TextField()),
                ('book_name', models.CharField(max_length=10)),
                ('return_date', models.TextField(max_length=20)),
                ('pub_time', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
    ]