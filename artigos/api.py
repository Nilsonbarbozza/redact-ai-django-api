from ninja import Router
from .models import Artigo
from .services import gerar_artigo
from django.shortcuts import get_object_or_404

router = Router()

@router.post("/gerar/")
def criar_artigo(request, titulo: str, categoria: str):
    conteudo = gerar_artigo(titulo, categoria)
    artigo = Artigo.objects.create(titulo=titulo, categoria=categoria, conteudo=conteudo)
    return {"id": artigo.id, "titulo": artigo.titulo, "conteudo": artigo.conteudo}

@router.get("/artigos/{artigo_id}/")
def obter_artigo(request, artigo_id: int):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    return {"titulo": artigo.titulo, "conteudo": artigo.conteudo, "categoria": artigo.categoria}
