from django.shortcuts import render


def index(request):
    """Main view of site"""
    return render(request, 'index.html')
