from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(Movie)
admin.site.register(Genres)
admin.site.register(Review)
admin.site.register(Cinema)