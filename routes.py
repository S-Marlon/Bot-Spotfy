from app import app
from app import redirect


@app.route("/")
def homepage():
    return "Servidor de redirecionamento de podcast ativo."

drive_id = "1CeOP_a7iSXW_imzGdhTM5dFVXECGhlz9"

@app.route("/audios")
def audios():
    return "pasta de audios"

@app.route(f"/audios/{drive_id}.mp3")
def audio():
    drive_id = "1CeOP_a7iSXW_imzGdhTM5dFVXECGhlz9"
    download_url = f"https://drive.google.com/uc?export=download&id={drive_id}"
    return redirect(download_url)