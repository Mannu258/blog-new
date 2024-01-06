from django import forms
from froala_editor.widgets import FroalaEditor
from tinymce.models import HTMLField
from .models import *

class Blogform(forms.ModelForm):
    class Meta:
        model = blogmodel
        fields = ['title','content']