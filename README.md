# Pasar-BackEnd

## install virtual envirotment
```
For Windows :
    python -m venv venv

For MacOS/Linux :
    python3 -m venv venv
```

## Activate a Virtual Enviroment
```
For Windows :
    .\venv\Scripts\activate

For MacOS/Linux :
    source venv/bin/activate
```

## install all the library at requierment.txt

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

## Crete Database
### create a database with a same name on DB_DATABASE variable in the file .env
### execute migration
```
Create Migration :
    flask db migrate -m "crete table"
Apply Migration :
    flask db upgrade
```

## running the program
```
flask run
```