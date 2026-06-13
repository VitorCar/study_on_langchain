from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# Carrega as variáveis do arquivo .env
load_dotenv()

chat_model = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0,
)

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content='Você deve responder baseado a um crítico de cinema'),
        HumanMessagePromptTemplate.from_template('Me fale sobre o filme {filme}.'),
        AIMessage(content='Claro, vou começar coletando informações sobre o filme sitado.'),
        HumanMessage(content='certifique-se de que a linguagem utilizada, seja uma linguagem coloquial, direta e acessível, focada na experiência do espectador comum.'),
        AIMessage(content='Entendido.')
    ]
)

prompt = chat_template.format_messages(filme='Interestelar')

response = chat_model.invoke(prompt)

print(response.content)
