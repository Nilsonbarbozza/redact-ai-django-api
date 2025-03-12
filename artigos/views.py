from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def criar_artigo(request):
    if request.method == "GET":
        return render(request, "artigos/criar_artigo.html")  # Renderiza o HTML

    elif request.method == "POST":
        try:
            data = json.loads(request.body)  # Captura os dados do formulário enviado via HTMX

            tema = data.get("titulo", "")
            palavras_chave = data.get("palavras_chave", "")
            funcoes = data.get("funcoes", [])

            # Simula a geração do artigo
            artigo_gerado = f"Artigo sobre {tema}, focado nas palavras-chave: {palavras_chave}. Profissões envolvidas: {', '.join(funcoes)}."

            return JsonResponse({"mensagem": "Artigo criado com sucesso!", "artigo": artigo_gerado})
        
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=400)

    return JsonResponse({"erro": "Método não permitido"}, status=405)

def dashboard(request):
    return render(request, "artigos/dashboard.html")

def settings(request):
    return render(request, "artigos/settings.html")
