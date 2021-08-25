# api_final_yatube

## Описание

**api_final_yatube** - это мой учебный проект по курсу Python-разработчик в Яндекс Практикуме.

Данный проект представляет из себя API, построенное на основе Django REST Framework. Это API для блог-платформы Yatube.

Тут можно писать посты, объединять их в группы, комментировать их и подписываться на авторов.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

``` bash
$ git clone https://github.com/m-dmit95/api_final_yatube.git
$ cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

``` bash
python3 -m venv env
source env/bin/activate
```

Установить зависимости из файла `requirements.txt`:

``` bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

``` bash
python3 manage.py migrate
```

Запустить проект:

``` bash
python3 manage.py runserver
```

Проект буден доступен по адресу *http://127.0.0.1:8000/*

## Некоторые примеры запросов к API

`api/v1/posts/`:
* **GET** - получить список постов
* **POST** - добавить свой пост

`api/v1/posts/{post_id}/comments/`:
* **GET** - получить список комментариев определенного поста
* **POST** - добавить комментарий к посту

Это далеко не весь список эндпоинтов и возможных запросов. В проекте есть документация к API в виде ReDoc - она доступна по адресу *http://127.0.0.1:8000/redoc/*.