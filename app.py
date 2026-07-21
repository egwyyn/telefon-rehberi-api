from flask import Flask

app = Flask(__name__)

@app.route("/")
def ana_sayfa():
    return "Telefon Rehberi API'ye Hos Geldiniz!"




if __name__ == "__main__":
    app.run(debug=True)