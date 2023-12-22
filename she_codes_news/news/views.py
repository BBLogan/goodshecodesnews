# News Setup Step 12: adding a new view
# Forms Setup Step 3: adding a new view for the form
# Users Setup Step 19: update the story creation view

# news/views
from typing import Any
from django.db import models
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from users.models import CustomUser
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(LoginRequiredMixin,generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditView(LoginRequiredMixin,generic.UpdateView):
    model = NewsStory
    form_class = StoryForm
    context_object_name = 'storyform-edit'
    template_name = 'news/editView.html'
    success_url = reverse_lazy('news:index')

class DeleteView(generic.DeleteView):
    model = NewsStory
    form_class = StoryForm
    context_object_name = 'storyform-delete'
    template_name = 'news/deleteView.html'
    success_url = reverse_lazy('news:index')

    def DeleteView(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class AuthorView(generic.DetailView):
    model = CustomUser
    template_name = 'news/authorView.html'
    context_object_name = 'author'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        context['latest_stories'] = NewsStory.objects.filter(author__id=author.id)
        return context