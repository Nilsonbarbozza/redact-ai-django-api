import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def gerar_artigo(titulo: str, palavras_chave: str, funcoes: list[str]) -> str:
    profissoes_escolhidas = ", ".join(funcoes) if funcoes else "público geral"
    
    prompt = f"""
    Escreva um artigo detalhado sobre "{titulo}" considerando as palavras-chave "{palavras_chave}".
    O artigo deve ser voltado para profissionais das seguintes áreas: {profissoes_escolhidas}.
    Utilize um tom informativo e envolvente.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Você é um assistente especialista em escrita."},
                  {"role": "user", "content": prompt}],
        max_tokens=1000
    )

    return response["choices"][0]["message"]["content"]
