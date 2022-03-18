# DJANGO REST FILTERING TUTORIAL

Source code for [Django REST Filtering Tutorial] series on [tech.serhatteker.com]

A simple application written in Python Django REST to demonstrate **filtering**.

* [part I]

## Setup Repo

```bash
# Create virtual environment named .venv
$ python -m venv ./.venv
# Activate the virtual environment
$ source ./.venv/bin/activate
# Install python packages
$ python -m pip install -r requirements.txt
# Create db, make migrations and seed database with some dummy data
$ python populate_db.py
# Run development server
$ python manage.py runserver 8000
# or
# ./manage.py runserver 8000
```

Also another option is that you can use [gnu make] and simply run:

```bash
$ make start
```

This **make** target will run all commands above together so it will setup the
repository and run development server.


## Main Endpoints

* `/users/`
* `/articles/`
* `/authors/`
* `/regions/`


## Sending HTTP Requests

With [httpie]:

```bash
$ http GET http://localhost:8000/authors/
# or with less keystroke, it's same as above
$ http :8000/authors/
```

With [curl]:

```bash
$ curl http://localhost:8000/authors/
```




[Django REST Filtering Tutorial]: https://tech.serhatteker.com/post/2022-03/django-rest-filtering-tutorial-part-1/
[part I]: https://tech.serhatteker.com/post/2022-03/django-rest-filtering-tutorial-part-1/
[tech.serhatteker.com]: https://tech.serhatteker.com/
[httpie]: https://httpie.io/
[curl]: https://curl.se/
[gnu make]: https://www.gnu.org/software/make/
