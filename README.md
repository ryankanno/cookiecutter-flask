# Introduction

This is a fairly opinionated [Flask](http://flask.pocoo.org) skeleton for
[Cookiecutter](https://github.com/audreyr/cookiecutter).

Heavily influenced by

  * [flask-skeleton](https://github.com/ryankanno/flask-skeleton)
  * [cookiecutter-py](https://github.com/ryankanno/cookiecutter-py)

# Topics

- [Main features](#main-features)
- [Quick start](#quick-start)
- [Usage](#usage)

# Main features

  * Automatically created pyenv-virtualenv
  * Teamocil file
  * Konch configuration
  * Bootstrap 3
  * User registration
  * Gulpfile
  * Logging configured with structlog

# Quick start

```
$ pip install cookiecutter
$ cookiecutter https://github.com/ryankanno/cookiecutter-flask
```

# Usage

To create your database:
  * `python manage.py createdb`

To drop your database:
  * `python manage.py dropdb`

To drop your database (without a prompt):
  * `python manage.py dropdb --force`
