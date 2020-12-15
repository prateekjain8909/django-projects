from django import forms
from . import models


class BlogForm(forms.ModelForm):
    class Meta:
        model= models.Blog
        fields = ["title", "content", "image"]

class CommentForm(forms.ModelForm):
    class Meta:
        model= models.Comment
        fields = ["name", "comment", "blog"]


class EditBlogForm(BlogForm):
    class Meta:
        model = models.Blog
        fields = ["title", "content", "image"]