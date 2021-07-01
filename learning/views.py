from django.shortcuts import render


def learning_view(request):
    return render(request, 'learning.html', {})
