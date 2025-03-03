from ninja import NinjaAPI #Importar NinjaAPI - para entender que é uma api
from artigos.api import router #rota para o app



api = NinjaAPI(title="Assistente de Escrita AI2")
api.add_router("/artigos/", router)