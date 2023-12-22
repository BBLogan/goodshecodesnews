# Forms Setup Step 1: creating a forms.py file
# Forms Setup Step 2: adding a ModelForm class
# Forms Setup Step 7: add a widget
# Users Setup Step 18: update the news story form

# news/forms.pyfields
from django import forms
from django.forms import ModelForm
from .models import NewsStory
from django.template.defaultfilters import mark_safe

class StoryForm(ModelForm):
    class Meta: 
        model = NewsStory
        fields = ['title', 'pub_date', 'content']
        widgets = {'pub_date': forms.DateInput(format='%m/%d/%Y', attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}
        # label = mark_safe()