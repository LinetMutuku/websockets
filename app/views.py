from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "AnonymousUser"

    context = {
        'username': username,
    }

    return render(request, 'index.html', context)
