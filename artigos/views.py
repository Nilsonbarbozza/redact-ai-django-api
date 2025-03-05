from django.shortcuts import render


def dashboard(request):
    return render(request, "artigos/dashboard.html")

def criar_artigo(request):
    return render(request, "artigos/criar_artigo.html")

def settings(request):
    return render(request, "artigos/settings.html")
