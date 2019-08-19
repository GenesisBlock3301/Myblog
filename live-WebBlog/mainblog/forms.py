from django import forms
from .models import *
from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    user_comment = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'What is your mind ?'}
    ),
        max_length=4000,
        help_text="the max length of text is 4000", )
    class Meta:
        model = Comment
        fields =('user_name' ,'user_email','user_comment')


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = "__all__"

    def clean_title(self):
        name = self.cleaned_data['title']
        if name.lower() == 'post' or name.lower() == 'add' or name.lower() == 'update':
            raise ValidationError("Post name can't be {}".format(name))
        return name