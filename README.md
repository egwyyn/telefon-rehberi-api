# 📖 Telefon Rehberi API

Flask ve SQLite kullanılarak geliştirilmiş basit bir Telefon Rehberi REST API projesidir.

## 🚀 Kullanılan Teknolojiler

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- Git

## 📂 Proje Yapısı

```
telefon-rehberi-api/
│
├── app.py
├── database.py
├── seed.py
├── requirements.txt
├── models/
├── routes/
└── instance/
```

## ⚙️ Kurulum

```bash
git clone <repo-url>

cd telefon-rehberi-api

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python seed.py

python app.py
```

## 📌 Endpointler

| Method | Endpoint | Açıklama |
|---------|----------|----------|
| GET | /kisiler | Tüm kişileri getir |
| GET | /kisi/<isim> | İsme göre kişi getir |
| GET | /sehir/<sehir> | Şehre göre kişileri getir |
| POST | /kisi | Yeni kişi ekle |
| DELETE | /kisi/<id> | Kişi sil |

