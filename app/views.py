from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html')


def about(request):
    return render(request, template_name='about.html')


def contact(request):
    return render(request, template_name='contact.html')


def services(request):
    return render(request, template_name='services.html')


def projects(request):
    return render(request, template_name='projects.html')

    
