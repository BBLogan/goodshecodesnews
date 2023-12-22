# News Setup Step 12: adding a new view
# Forms Setup Step 5: add a URL for our form page

# news/urls.py
from django.urls import path
from . import views
from .views import delete_story

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('<int:pk>/edit-story/', views.EditView.as_view(), name='editStory'),
    path('delete-story/<int:story_id>/', delete_story, name='delete_story'),
    path('author/<str:username>', views.AuthorView.as_view(), name='authorView'),
]