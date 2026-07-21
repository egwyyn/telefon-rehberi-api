from flask import Flask
from database import db
from models.contact import Contact

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rehber.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def ana_sayfa():
    return "Telefon Rehberi API'ye Hoş Geldiniz!"

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)