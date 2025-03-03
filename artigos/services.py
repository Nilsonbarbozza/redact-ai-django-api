import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def gerar_artigo(titulo, categoria):
    prompt = f"Escreva um artigo sobre {titulo} na categoria {categoria}. O artigo deve ser otimizado para Medium e conter informações relevantes."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um redator experiente."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
