# DJANGO REST FILTERING TUTORIAL

Source code for [Django REST Filtering Tutorial] series on [tech.serhatteker.com]

A simple application written in Python Django REST to demonstrate **filtering**.

* [Tutorial part I]
* [Tutorial part II]
* [Tutorial part III]

You can find related branches to the tutorial parts.

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

Also another option is that you can use [gnu make], simply run:

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


## Authentication and Permission

Authentication and permission disabled by default. In order to enable them
comment out related lines at the end of the `settings.py` file.

You can make a successful request by including the username and password of
one of the users created in `populate_db.py`:

```bash
$ http -a User1:1234 :8000/authors

[
    {
        "first_name": "Name1",
        "full_name": "Name1 Surname1",
        "id": 1,
        "last_name": "Surname1",
        "user": 1
    },
    {
        "first_name": "Name2",
        "full_name": "Name2 Surname2",
        "id": 2,
        "last_name": "Surname2",
        "user": null
    },
    {
        "first_name": "Name3",
        "full_name": "Name3 Surname3",
        "id": 3,
        "last_name": "Surname3",
        "user": 3
    }
]
```

All 3 users and their passwords:
- `User1:1234`
- `User2:1234`
- `User3:1234`




[Django REST Filtering Tutorial]: https://tech.serhatteker.com/post/2022-03/django-rest-filtering-tutorial-part-1/
[tech.serhatteker.com]: https://tech.serhatteker.com/
[httpie]: https://httpie.io/
[curl]: https://curl.se/
[gnu make]: https://www.gnu.org/software/make/
[Tutorial part I]: https://tech.serhatteker.com/post/2022-03/django-rest-filtering-tutorial-part-1/
[Tutorial part II]: https://tech.serhatteker.com/post/2022-03/django-rest-filtering-tutorial-part-2/
[Tutorial part II]: https://tech.serhatteker.com/post/2022-03/django-rest-filtering-tutorial-part-3/
