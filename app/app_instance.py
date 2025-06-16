from flask import Flask
app = Flask(__name__)
from app.logic.drive import listar_arquivos

itens = []

def pega():
    arquivos = listar_arquivos()
    global itens
    itens = arquivos
    return itens