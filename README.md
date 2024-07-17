# Курсовая работа 7 DRF

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена
приобретению новых полезных привычек и искоренению старых плохих привычек.
Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать
трекер полезных привычек.
В рамках учебного курсового проекта реализуйте бэкенд-часть SPA веб-приложения.


Клонирование проекта
git clone https://github.com/AleksandrZaec/CourseDRF.git

Заполните файл .env своими данным по примеру .env_example

Сборка и запуск контейнеров

docker-compose up --build

Регистрация нового пользователя http://127.0.0.1:8000/users/create/ {POST}
{ "email": "user@example.com", "password": "Somepassword", "telegram_id": "000000001", "telegram_nik": "@primerPrimerov" }

Получение токена http://127.0.0.1:8000/users/token/
Создание привычки http://127.0.0.1:8000/habits/create/
{ "place": "на улице", "time": "10:00", "action": "погулять", "is_enjoyable": false, "periodicity": 3, # по выходным "treat": "поиграть в пк", "duration": 120, "is_public": true }

Документация

Swagger - http://127.0.0.1:8000/docs/

Redoc - http://127.0.0.1:8000/redoc/