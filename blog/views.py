from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog.forms import AddBlogForm
from blog.models import BlogModel


def blog_view(request):
    context_blog = BlogModel.objects
    if request.method == 'POST':
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.image = request.FILES['image']
            new_form.save()
            return HttpResponseRedirect('/blog')
    else:
        form = AddBlogForm()
    return render(request, 'blog.html', {'form': form, 'context': context_blog})


def blog_delete_view(request, blog_id):
    blog = BlogModel.objects.get(pk=blog_id)
    if request.method == 'POST':
        blog.image.delete()
        blog.delete()
        return HttpResponseRedirect('/blog')
    return render(request, 'delete_blog.html', {'blog': blog})


def blog_wholly_view(request, blog_id):
    blog = BlogModel.objects.get(pk=blog_id)
    return render(request, 'wholly_blog.html', {'blog': blog})
