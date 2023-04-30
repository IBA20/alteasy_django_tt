# Сервис для управления списком книг  

Пример работающего сайта: [books.3m.ru](https://books.3m.ru)  
Используйте логин admin, пароль admin

## Локальная установка и запуск

1. Клонируйте данный репозиторий.  
```sh
git clone https://github.com/devmanorg/alteasy_django_tt.git
```
2. Создайте виртуальное окружение и установите зависимости:  
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. В корне проекта создайте файл .env со следующим содержимым:  
```
SECRET_KEY - cекретный ключ Django
DATABASE_URL - при использовании БД, отличной от sqlite (пример: postgres://USER:PASSWORD@HOST:PORT/NAME)
```
4. Создайте базу данных и отмигрируйте её следующей командой:  
```sh
python manage.py migrate
```
5. Создайте профиль администратора:  
```sh
python manage.py createsuperuser
```
6. Запустите сервер:  
```sh
python manage.py runserver
```
Откройте сайт в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/) и/или админ-панель по адресу [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Цели проекта

Код представляет собой решение тестового задания компании Alteasy

