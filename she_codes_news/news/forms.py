# Forms Setup Step 1: creating a forms.py file
# Forms Setup Step 2: adding a ModelForm class
# Forms Setup Step 7: add a widget
# Users Setup Step 18: update the news story form

# news/forms.py
from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta: 
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'img_url']
        widgets = {'pub_date': forms.DateInput(format='%d/%m/%Y %H:%M', 
                attrs={
                    'class':'form-control', 
                    'placeholder':'Select a date', 
                    'type':'datetime-local'}),}