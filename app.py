from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Ayuda no entiendo nada"

if __name__ == "__main__":
    app.run()