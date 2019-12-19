from django.contrib import admin
from .models import MovieDirector, Movie, Actor, Review


admin.site.register(MovieDirector)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Review)

