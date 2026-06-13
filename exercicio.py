from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from interface_exercicio import interface


load_dotenv()

chat_model = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0,
)

# Lendo o pdf
loader = PyPDFLoader('musculacao_jovens_saude_autoestima.pdf')
documents = loader.load()

# Percorrendo Documento 
scrolling_through_document = "\n\n".join(doc.page_content for doc in documents)

sort_text_size = (
    ChatPromptTemplate.from_messages(
        [
            (
                'ai',
                """
                Classifique a resposta do usuário em uma das seguintes opções:
                - Resumo Curto
                - Resumo Detalhado
                """
            ),
            (
                'human',
                'resposta: {resposta}'
            ),
        ]
    )
    | chat_model
    | StrOutputParser()
)

short_summary = (
    ChatPromptTemplate.from_messages(
        [
            (
                'ai',
                '''
                Você é um sistema que lê arquivos (PDF, TXT, CSV, etc.) e, através desta leitura, gera um resumo curto do conteúdo do arquivo. 
                Principais regras: 
                - Sempre gere um resumo começando com "Bem-vindo ao Sistema de Resumos(Curtos) Vitor"
                - resumo conciso (até 80 palavras)
                - 3–5 tópicos-chave, OBS: tem que está em uma parte separada do resumo
                - Tenha no final uma linha escrita 'Contagem_de_palavras:' em destaque, contendo o número(inteiro) de palavras utilizadas.
                conteudo: {conteudo}
                '''
            ),
            (
                'human',
                'resposta: {resposta}'
            ),
        ]
    )
    | chat_model
    | StrOutputParser()
)

detailed_summary = (
    ChatPromptTemplate.from_messages(
        [
            (
                'ai',
                '''
                Você é um sistema que lê arquivos (PDF, TXT, CSV, etc.) e, através desta leitura, gera um resumo curto do conteúdo do arquivo. 
                Principais regras: 
                - Sempre gere um resumo começando com "Bem-vindo ao Sistema de Resumos(Detalhados) Vitor"
                - resumo detalhado (~200–250 palavras) 
                - 5–7 tópicos-chave, OBS: tem que está em uma parte separada do resumo
                - Tenha no final uma linha escrita 'Contagem_de_palavras:' em destaque, contendo o número(inteiro) de palavras utilizadas.
                conteudo: {conteudo}
                '''
            ),
            (
                'human',
                'resposta: {resposta}'
            ),
        ]
    )
    | chat_model
    | StrOutputParser()
)

def route(text_size):
    text_size = text_size.lower()
    if 'curto' in text_size:
        return short_summary
    else:
        return detailed_summary

question = interface()

# mandar a resposta do usuário
summary = sort_text_size.invoke(
    {'resposta': question}
)

# Este comando retorna o resultado do sort_text_size def route(retornou para cá):
response_summary = route(text_size=summary)

response = response_summary.invoke(
    {
        'conteudo': scrolling_through_document,
        'resposta': question
    }
)

print(response)
