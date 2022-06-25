from django.shortcuts import render

# Create your views here.

def home(request, *args, **kwargs):
    context = {
        'title' : 'Home'
    }
    return render(request, "home.html", context)


# def blog(request, *args, **kwargs):
#     context = {
#         'title' : 'Blog'
#     }
#     return render(request, "blog.html", context)


def contact(request, *args, **kwargs):
    context = {
        'title' : 'Contact'
    }
    return render(request, "contact.html", context)


def passwordGenerator(request, *args, **kwargs):
    context = {
        'title': 'Password Generator',
    }

    return render(request, 'passwordGenerator.html', context)
