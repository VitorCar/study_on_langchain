# Caching de prompts
# pip install langchain_community
# InMemoryCache -> Fica só na memoria ram se parar o script ele NÃO tem mais este cache NÃO E MAIS UTILIZADO
# SQLiteCache -> Vai salvar em um banco sqlite, mesmo parando o script a resposta estará salva 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.caches import InMemoryCache    # Se moveu para o core
from langchain_community.cache import SQLiteCache # Continua no community
from langchain_core.globals import set_llm_cache


# Carrega as variáveis do arquivo .env
load_dotenv()

chat_model = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0,
    max_tokens=120,
)

set_llm_cache(
    SQLiteCache(
        database_path='openai_cache.db',
        #allowed_objects=("messages",)  # Garante segurança e remove o alerta
    )
)      # (InMemoryCache()) # Estou dizendo para o langchain utilizar cache em memoria 

prompt = 'Me diga que foi michael jackson em 600 caracteres.' # michael jackson

response_1 = chat_model.invoke(prompt)
print(f'Chamada 1: {response_1.content}')

print('-' * 180)

response_2 = chat_model.invoke(prompt)
print(f'\nChamada 2: {response_2.content}')
