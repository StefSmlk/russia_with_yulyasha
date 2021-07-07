from django import forms

from blog.models import BlogModel


class AddBlogForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ('name', 'image', 'description')
