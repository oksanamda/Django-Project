from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'movie'


urlpatterns = [
    # /directors/
    path('', views.IndexView.as_view(), name="index"),

    # /directors/'name'
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),

    # /directors/add
    path('add/', views.DirectorCreate.as_view(), name='d-add'),

    # /directors/1/update
    path('<int:pk>/update/', views.DirectorUpdate.as_view(), name='d-update'),

    # /directors/2/delete
    path('<int:pk>/delete/', views.DirectorDelete.as_view(), name='d-delete'),

    #/directors/movies
    path('movies/',views.IndexMovie.as_view(), name="index_movie"),

    #/directors/movies/1
    path('movies/<int:pk>/', views.DetailMovie.as_view(), name="detail_movie"),

    # /directors/movies/add
    path('movies/add/', login_required(views.MovieCreate.as_view()), name='m-add'),

    # /directors/movies/1/update
    path('movies/<int:pk>/update/', login_required(views.MovieUpdate.as_view()), name='m-update'),

    # /directors/movies/2/delete
    path('movies/<int:pk>/delete/', login_required(views.MovieDelete.as_view()), name='m-delete'),

    # /directors/actors/add
    path('actors/add/', login_required(views.ActorCreate.as_view()), name='a-add'),

    # /directors/actors/1/update
    path('actors/<int:pk>/update/', login_required(views.ActorUpdate.as_view()), name='a-update'),

    # /directors/actors/2/delete
    path('actors/<int:pk>/delete/', login_required(views.ActorDelete.as_view()), name='a-delete'),

    # /directors/movies/review/add/
    path('movies/review/<int:movie_id>/add/', views.add_review, name='add_review'),

    # /director/movies/reviews/1/delete/
    path('movies/review/<int:pk>/update/', views.update_review, name='update_review'),
    # /director/movies/reviews/1/delete/
    path('movies/review/<int:pk>/delete/', views.DeleteReview.as_view(), name='delete_review'),
]