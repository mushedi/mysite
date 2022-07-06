from django.shortcuts import render

# Create your views here.

class Pages():
    def home(request, *args, **kwargs):
        context = {
            'title' : 'Home'
        }
        return render(request, "home.html", context)


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
