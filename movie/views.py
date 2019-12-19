from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MovieDirector, Movie, Actor, Review
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from django.contrib import messages
from django.http import HttpResponseForbidden


class IndexView(generic.ListView):
    template_name = 'movie/index.html'
    context_object_name = 'all_directors'

    def get_queryset(self):
        return MovieDirector.objects.all()


class DetailView(generic.DetailView):
    model = MovieDirector
    template_name = 'movie/detail.html'


class DirectorCreate(LoginRequiredMixin, CreateView):
    model = MovieDirector
    fields = ['name', 'surname', 'birthday', 'country', 'photo', 'is_alive']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DirectorUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MovieDirector
    fields = ['name', 'surname', 'birthday', 'country', 'photo', 'is_alive']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        moviedirector = self.get_object()
        if self.request.user == moviedirector.author:
            return True
        return False


class DirectorDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MovieDirector
    success_url = reverse_lazy('movie:index')

    def test_func(self):
        moviedirector = self.get_object()
        if self.request.user == moviedirector.author:
            return True
        return False


class IndexMovie(generic.ListView):
    template_name = 'movie/index_movie.html'
    context_object_name = 'all_movies'

    def get_queryset(self):
        return Movie.objects.all()


class DetailMovie(generic.DetailView):
    model = Movie
    template_name = 'movie/detail_movie.html'


class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['director', 'title', 'year', 'genre', 'poster']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MovieUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    fields = ['director', 'title', 'year', 'genre', 'poster']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.author:
            return True
        return False


class MovieDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    success_url = reverse_lazy('movie:index_movie')

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.author:
            return True
        return False


class ActorCreate(LoginRequiredMixin, CreateView):
    model = Actor
    fields = ['movie', 'name', 'surname', 'birthday', 'country', 'is_alive']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ActorUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Actor
    fields = ['movie', 'name', 'surname',  'birthday', 'country', 'is_alive']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        actor = self.get_object()
        if self.request.user == actor.author:
            return True
        return False


class ActorDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Actor
    success_url = reverse_lazy('movie:index_movie')

    def test_func(self):
        actor = self.get_object()
        if self.request.user == actor.author:
            return True
        return False


def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        author = Review(author=request.user)
        form = ReviewForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your review has been created!')
            return redirect('movie:detail_movie', pk=movie.pk)
    else:
        form = ReviewForm
    return render(request, 'movie/review_form.html', {'form': form})


def update_review(request, pk):
    currentReview = Review.objects.get(pk=pk)
    slug = currentReview.movie_id
    if currentReview.author == request.user:
        initial = {'movie': currentReview.movie,
                   'rating': currentReview.rating,
                   'title': currentReview.title,
                   'review': currentReview.review}
        form = ReviewForm(request.POST or None,initial=initial, instance=request.user)
        if form.is_valid():
            currentReview.rating = form.cleaned_data['rating']
            currentReview.title = form.cleaned_data['title']
            currentReview.review = form.cleaned_data['review']
            currentReview.save()
            messages.success(request, f'Your review has been updated successfully')
            return redirect('movie:detail_movie', pk=slug)
        return render(request, 'movie/review_form.html', {'form': form})
    else:
        return HttpResponseForbidden()


class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('movie:index_movie')

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False
