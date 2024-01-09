from django.apps import AppConfig

import sqlite3

class MysiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysite'

from django.shortcuts import render


