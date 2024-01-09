# Generated by Django 4.2.6 on 2023-10-29 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200)),
                ('author1', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Function1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Function2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=200)),
                ('activitypeople', models.CharField(max_length=200)),
                ('activityplace', models.CharField(max_length=200)),
                ('activitycontant', models.CharField(max_length=200)),
                ('activitynotice', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
