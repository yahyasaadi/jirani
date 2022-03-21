from django import forms
from .models import Neighborhood, Post

class HoodForm(forms.ModelForm):

    class Meta:
        model = Neighborhood
        fields = ['hood_name', 'hood_location']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'post']