from django.shortcuts import render

def index(request):
    message = {
        'text':'Hello',
    }
    return render(request, 'blog/index.html', message)