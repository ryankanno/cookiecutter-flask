# Introduction

A [cookiecutter](https://github.com/audreyr/cookiecutter) for [Flask](http://flask.pocoo.org).

# Topics

- [Features](#features)
- [Quick start](#quick-start)
- [Usage](#usage)

## Features

  * For Flask 0.10.1
  * Twitter [Bootstrap](http://getbootstrap.com) 3
  * Customized user registration
  * Gulp w/ Webpack integration
  * Logging configured via structlog
  * Automatic pyenv-virtualenv creation
  * Automatic teamocil file
  * Konch configuration

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
