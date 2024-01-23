# Pasar-BackEnd

## instal virtual envirotment
```
Untuk Windows
python -m venv venv

Untuk MacOS/Linux
python3 -m venv venv
```

## Aktifkan Virtual Enviroment
```
Untuk Windows
.\venv\Scripts\activate

Untuk MacOS/Linux
source venv/bin/activate
```

## install library all at requierment.txt

## add .env file
```
FLASK_APP = server.py
FLASK_ENV = development
FLASK_DEBUG = True

JWT_SECRET = xxxxxxx

DB_HOST     = 
DB_DATABASE = 
DB_USERNAME = 
DB_PASSWORD = 
```

## running the program
```
flask run
```