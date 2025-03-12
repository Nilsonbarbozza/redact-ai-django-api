from ninja import Router
from .models import Artigo
from .services import gerar_artigo
from django.shortcuts import get_object_or_404

router = Router()

@router.post("/criar_artigo/")
def criar_artigo(request, titulo: str, palavras_chave: str, funcoes: list[str]):
    conteudo = gerar_artigo(titulo, palavras_chave, funcoes)
    return {"titulo": titulo, "conteudo": conteudo}

@router.get("/artigos/{artigo_id}/")
def obter_artigo(request, artigo_id: int):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    return {"titulo": artigo.titulo, "conteudo": artigo.conteudo, "categoria": artigo.categoria}
