from flask import Blueprint, request
from database import db
from models.contact import Contact

contact_bp = Blueprint("contact", __name__)


# Tüm kişileri getir
@contact_bp.route("/kisiler", methods=["GET"])
def kisileri_getir():

    kisiler = Contact.query.all()

    sonuc = []

    for kisi in kisiler:
        sonuc.append(kisi.to_dict())

    return sonuc


# İsme göre kişi getir
@contact_bp.route("/kisi/<isim>", methods=["GET"])
def kisi_getir(isim):

    kisi = Contact.query.filter_by(isim=isim).first()

    if kisi:
        return kisi.to_dict()

    return {"hata": "Kişi bulunamadı."}, 404


# Şehre göre kişileri getir
@contact_bp.route("/sehir/<sehir>", methods=["GET"])
def sehire_gore_kisiler(sehir):

    kisiler = Contact.query.filter_by(sehir=sehir).all()

    sonuc = []

    for kisi in kisiler:
        sonuc.append(kisi.to_dict())

    return sonuc


# Yeni kişi ekle
@contact_bp.route("/kisi", methods=["POST"])
def kisi_ekle():

    veri = request.get_json()

    yeni_kisi = Contact(
        isim=veri["isim"],
        soyisim=veri["soyisim"],
        telefon=veri["telefon"],
        sehir=veri["sehir"]
    )

    db.session.add(yeni_kisi)
    db.session.commit()

    return {
        "mesaj": "Kişi başarıyla eklendi."
    }, 201


# ID'ye göre kişi sil
@contact_bp.route("/kisi/<int:id>", methods=["DELETE"])
def kisi_sil(id):

    kisi = db.session.get(Contact, id)

    if kisi is None:
        return {
            "hata": "Kişi bulunamadı."
        }, 404

    db.session.delete(kisi)
    db.session.commit()

    return {
        "mesaj": "Kişi silindi."
    }