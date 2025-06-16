from app_instance import app,pega
from main import main
from routes import *


# def rotina: terá um timer que executará o app de tempos em tempos
def init():
    main()
    
    

if __name__ == "__main__":
    app.run(debug=True)