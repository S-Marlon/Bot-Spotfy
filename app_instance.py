from flask import Flask
app = Flask(__name__)

itens = []

def pega(data):
    global itens
    itens = data