from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langserve import add_routes
from dotenv import load_dotenv,find_dotenv
import uvicorn
import os

_ = load_dotenv(find_dotenv())

os.environ['MISTRAL_API_KEY']  = os.getenv('MISTRAL_API_KEY')


app = FastAPI(
    title='Langchain Server',
    version= "0.1",
    description='A simple API Server',
    ssl_certfile="cert.pem",
    ssl_keyfile="key.pem"
)

add_routes(
    app,
    ChatMistralAI(),
    path = '/mistralAI'
)


model = ChatMistralAI()
promptV1 = ChatPromptTemplate.from_template(
    template='Provide me an essay about {topic}',
)

promptV2 = ChatPromptTemplate.from_template(
    template='Provide me an poem about {topic}',
)

add_routes(
    app,
    promptV1 | model,
    path = '/essay'
)

add_routes(
    app,
    promptV2 | model,
    path = '/poem'
)

if __name__ == '__main__':
    uvicorn.run(app, host = 'localhost',port = 8000 , ssl_keyfile='key.pem',
        ssl_certfile='cert.pem')