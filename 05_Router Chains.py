from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser # (Extrai a string de dentro do AIMessage) não precisa mais de .content
from langchain_core.prompts import ChatPromptTemplate


# Carrega as variáveis do arquivo .env
load_dotenv()

chat_model = ChatOpenAI(
    model='gpt-4o-mini',
)

classification_chain = (
    ChatPromptTemplate.from_messages(
        [
            (
                'ai',
                """
                Classifique a pergunta do usuário em um dos seguintes setores:
                - Financeiro
                - Suporte Técnico
                - Outras Informações
                """
            ),
            (
                'human',
                'Pergunta: {pergunta}'
            ),
        ]
    )
    | chat_model
    | StrOutputParser()
)

financial_chain = (
    ChatPromptTemplate.from_messages(
        [
            (
                'ai',
                """
                Você é um especialista financeiro.
                Sempre responda ás perguntas começando com "Bem-vindo ao Setor Financeiro".
                Responda a pergunta do usuário:
                """
            ),
            (
                'human',
                'Pergunta: {pergunta}'
            )
        ]
    )
    | chat_model
    | StrOutputParser()
)

tech_support_chain = (
    ChatPromptTemplate.from_messages(
        [
            (
                'ai',
                """
                Você é um especialista em suport técnico.
                Sempre responda ás perguntas começando com "Bem-vindo ao Suporte Técnico".
                Responda a pergunta do usuário:
                """
            ),
            (
                'human',
                'Pergunta: {pergunta}'
            )
        ]
    )
    | chat_model
    | StrOutputParser()
)

other_info_chain = (
    ChatPromptTemplate.from_messages(
        [
            (
                'ai',
                """
                Você é um assistente de informações gerais.
                Sempre responda ás perguntas começando com "Bem-vindo ao setor de Central de Informações".
                Responda a pergunta do usuário:
                """
            ),
            (
                'human',
                'Pergunta: {pergunta}'
            )
        ]
    )
    | chat_model
    | StrOutputParser()
)

# Criando o router
def route(classification):
    classification = classification.lower() # Tudo em minusculo
    if 'financeiro' in classification:
        return financial_chain
    elif 'técnico' in classification:
        return tech_support_chain
    else:
        return other_info_chain 
    
pergunta = str(input('Faça uma pergunta?'))

classification = classification_chain.invoke(
    {'pergunta': pergunta}
)

# Este comando retorna o resultado do classification_chain def route(retornou para cá):
response_chain = route(classification=classification)

response = response_chain.invoke(
    {'pergunta': pergunta}
)

print(response)
