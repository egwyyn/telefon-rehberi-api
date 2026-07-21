from database import db

class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    isim = db.Column(db.String(50), nullable=False)
    soyisim = db.Column(db.String(50), nullable=False)
    telefon = db.Column(db.String(20), nullable=False)
    sehir = db.Column(db.String(50), nullable=False)