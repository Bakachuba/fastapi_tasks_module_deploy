Приложение для планирования

(Составной тестировачный модуль для сайта)

Команды для запуска локально:

1) pip install -r requirements.txt
2) uvicorn main:app --reload

Команды для запуска на сервере:
1) docker build . --tag fastapi
2) docker run -p 80:80 fastapi

Или
1) docker build . --tag fastapi_app && docker run -p 80:80 fastapi_app 

Основные функции:

1) трекер
2) планирование