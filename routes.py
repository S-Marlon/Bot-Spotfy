from app import app
from app import redirect
from sum import *


@app.route("/")
def homepage():
    result = soma(5,2)
    return f"Servidor de redirecionamento de podcast ativo. {result}"

drive_id = "1PBhSNrIoSrv0zBnYlrGdj1OedDAwftCJ"

@app.route("/audios")
def audios():
    return "pasta de audios"

@app.route(f"/audios/{drive_id}.mp3")
def audio():
    drive_id = "1PBhSNrIoSrv0zBnYlrGdj1OedDAwftCJ"
    download_url = f"https://drive.google.com/uc?export=download&id={drive_id}"
    return redirect(download_url)