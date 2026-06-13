from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser # (Extrai a string de dentro do AIMessage) não precisa mais de .content
from langchain_core.prompts import ChatPromptTemplate


# Carrega as variáveis do arquivo .env
load_dotenv()

chat_model = ChatOpenAI(
    model='gpt-4o-mini',
)

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um assistente técnico. Responda em apenas uma frase."),
        ("human", "O que é {conceito}?")
    ]
)

# Ele entende que tem que rodar o objeto chat_template dentro do chat_model e o retorno tem que ser so o texto 
runnable_sequence = chat_template | chat_model | StrOutputParser()

response = runnable_sequence.invoke({'conceito': 'Chains'})

print(response)

# Outro Modo:

# runnable_sequence = (
#     ChatPromptTemplate.from_messages(
#         ("system", "Você é um assistente técnico. Responda em apenas uma frase."),
#         ("human", "O que é {conceito}?")
#     )
#     | chat_model
#     | StrOutputParser
# )

# response = runnable_sequence.invoke({'conceito': 'API'})

# print(response)
