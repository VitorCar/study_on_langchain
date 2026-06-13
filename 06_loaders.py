from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser # (Extrai a string de dentro do AIMessage) não precisa mais de .content
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader


# Carrega as variáveis do arquivo .env
load_dotenv()

chat_model = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0  # Para RAG, temperature 0 garante respostas factuais e evita alucinações
)

# loader = TextLoader('base_conhecimento.txt', encoding='utf-8')
# documents = loader.load()

# loader = PyPDFLoader('base_conhecimento.pdf', encoding='utf-8')
# documents = loader.load()

# 3. Carregamento da Base de Conhecimento
# Boa prática: sempre force o encoding 'utf-8' para evitar quebras com acentos locais
loader = CSVLoader('base_conhecimento.csv', encoding='utf-8')
documents = loader.load()

# Usar "\n\n" separa melhor as linhas/registros do CSV para o contexto da IA
contexto_consolidado = "\n\n".join(doc.page_content for doc in documents)

#contexto = '\n'.join(doc.page_content for doc in documents),  # Caso tenha que ler mais de um documento este join percorre os documentos linha po linha 

# 4. Estruturação do Prompt Moderno (ChatPromptTemplate)
# O LangChain moderno descobre as variáveis automaticamente, dispensando o 'input_variables'
prompt_base_conhecimento = ChatPromptTemplate.from_messages([
    (
        "system", 
        "Use o seguinte contexto para responder à pergunta.\n"
        "Responda apenas com base nas informações fornecidas.\n"
        "Não utilize informações externas ao contexto.\n\n"
        "Contexto:\n{contexto}"
    ),
    (
        "human", 
        "{pergunta}"
    )
])

chain = prompt_base_conhecimento | chat_model | StrOutputParser()


# 6. Execução do pipeline de RAG
response = chain.invoke({
    'contexto': contexto_consolidado,
    'pergunta': 'Quais são os carros?'
})

print(response)
