from django.shortcuts import render

def home_page(request):
    '''Home page'''
    return render(request, "home.html")