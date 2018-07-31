# catalog_foto
Каталог фото

Для запуска нужен python3, virtualenvwrapper, mysql:
 1) Клонируем репозиторий git clone https://github.com/Sergey19940808/catalog_foto.git
 1) Создаём виртуальное окружение mkvirtualenv name_venv -p /usr/bin/python3;
 2) Создаём базу данных с именем CatalogFoto - (выполняем команды 1) mysql -u user -p password; 2) CREATE DATABASE CatalogFoto );
 3) Заходим в каталог cd catalog_foto и выполняем pip -r install requirements.txt (убедитесь что вы активировали виртуальное окружение);
 4) Создаём все нужные таблицы в БД python manage.py migrate;
 5) Запускаем сервер python manage.py runserver и пользуемся!);
