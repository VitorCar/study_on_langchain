from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


# Carrega as variáveis do arquivo .env
load_dotenv()

# 1. Instanciamos o modelo de Chat (Padrão da indústria)
# As configurações de comportamento ficam na construção do objeto
chat_model = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=1,
    max_tokens=120,
)

input_text =[
    {'role':'system',
     'content': 'Você e um escritor grande fã e estudioso sobre a literatura russa.'
    },
    {'role': 'user',
     'content': " Descreva para uma pessoa leiga utilizando 200 caracteres, quem foi fiodor dostoievski."
    }
] 

response = chat_model.invoke(input_text)

# print(response)
print(response.content)