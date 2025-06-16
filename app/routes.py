import random
from flask import redirect, render_template
from app.app_instance import app,pega
from app.app import init

def soma(soma1,soma2):
    result = soma1 + soma2
    return result

@app.route("/")
def homepage():
    result = soma(random.randint(1, 30),random.randint(1, 30))
    return render_template("index.html")

@app.route("/feed")
def feedrss():
    return render_template("rss.xml")

@app.route("/start", methods=["POST"])
def start():
    
    print("▶️ Aplicação iniciada")
    
    init()
    
    return "✅ Aplicação iniciada com sucesso!"

@app.route("/audios")
def audios():
    return "pasta de audios"

#def rota não esta conseguindo baixar corretamente
# provavelmente não recebe o iten atualizado de dhare.py
@app.route("/audios/<drive_id>.mp3")
def audio(drive_id):
    itens = pega()
    
    print(f"vai toma {itens}")
    for item in itens:
        if item["id"] == drive_id:
            download_url = f"https://drive.google.com/uc?export=download&id={item['id']}"
            return redirect(download_url)
        else:
            return "nenhum video foi encontrado"
    return "nenhum video foi encontssrado"
        
    
