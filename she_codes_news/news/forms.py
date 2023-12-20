# Forms Setup Step 1: creating a forms.py file
# Forms Setup Step 2: adding a ModelForm class

# news/forms.py
from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta: 
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content']