from app import app
from database import db
from models.contact import Contact

with app.app_context():

    # Eski kayıtları sil
    Contact.query.delete()

    kisiler = [
        Contact(isim="Ahmet", soyisim="Yılmaz", telefon="05551234567", sehir="İzmir"),
        Contact(isim="Mehmet", soyisim="Kaya", telefon="05321234567", sehir="Aydın"),
        Contact(isim="Ayşe", soyisim="Demir", telefon="05431234567", sehir="Muğla"),
        Contact(isim="Fatma", soyisim="Çelik", telefon="05531234567", sehir="Ankara"),
        Contact(isim="Ali", soyisim="Şahin", telefon="05051234567", sehir="İstanbul"),
        Contact(isim="Zeynep", soyisim="Acar", telefon="05351234567", sehir="Bursa"),
        Contact(isim="Hasan", soyisim="Koç", telefon="05451234567", sehir="Antalya"),
        Contact(isim="Elif", soyisim="Arslan", telefon="05571234567", sehir="Eskişehir"),
        Contact(isim="Murat", soyisim="Yıldız", telefon="05071234567", sehir="Denizli"),
        Contact(isim="Ece", soyisim="Öztürk", telefon="05371234567", sehir="Balıkesir"),
    ]

    db.session.add_all(kisiler)
    db.session.commit()

    print("10 kişi başarıyla eklendi.")