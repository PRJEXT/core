from fastapi import FastAPI, HTTPException
from pydantic import BaseModel # pylint: disable=no-name-in-module

from service.SentAnalysis import SentAnalysis

app = FastAPI()

svc = SentAnalysis()


class Item(BaseModel):
    '''Classe que representa a requisição (item) que será analisada.
    Extende a classe BaseModel que "envelopa" a requisição em um JSON.
    Dentro desta classe são definidos os atributos da requisição.
    '''
    text: str
    grade: int


@app.post('/', tags=['sentment_analysis'])
def analise_review(item: Item):
    '''Método responsável por receber e responder a requisição,
    chamando o analisador de sentimentos.
    '''
    return svc.predict(item.text)
