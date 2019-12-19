from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError


class MovieDirector(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateField(default=date.today)
    country = models.CharField(max_length=100)
    photo = models.FileField()
    is_alive = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('movie:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + ' ' + self.surname


class Movie(models.Model):
    director = models.ForeignKey(MovieDirector, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2020)])
    genre = models.CharField(max_length=100)
    poster = models.FileField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('movie:detail_movie', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' ' + str(self.year)


class Actor(models.Model):
    movie = models.ManyToManyField(Movie)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateField(default=date.today)
    country = models.CharField(max_length=100)
    is_alive = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('movie:index_movie')

    def __str__(self):
        return self.name + ' ' + self.surname


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='review', on_delete=models.CASCADE)
    RATINGS = (
        (1, '1 Star'),
        (2, '2 Star'),
        (3, '3 Star'),
        (4, '4 Star'),
        (5, '5 Star')
    )
    rating = models.IntegerField(choices=getattr(settings, 'REVIEW_RATING_CHOICES', RATINGS))
    title = models.CharField(max_length=100)
    review = models.TextField()

    def validate_unique(self, *args, **kwargs):
        super(Review, self).validate_unique(*args, **kwargs)

        if self.__class__.objects.\
                filter(author=self.author, movie=self.movie).\
                exists():
            raise ValidationError(
                message='Your review for this movie already exists.',
                code='unique_together',
            )

    def __str__(self):
        return self.title



