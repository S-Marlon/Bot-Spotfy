from app_instance import app,pega
from main import main
from routes import *


# def rotina: terá um timer que executará o app de tempos em tempos
def init():
    data = main()
    print(f"data é {data}")
    pega(data)

if __name__ == "__main__":
    app.run(debug=True)