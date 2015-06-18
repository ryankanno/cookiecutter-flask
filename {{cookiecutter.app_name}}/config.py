#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from {{cookiecutter.app_name}}.apps.www import www
from {{cookiecutter.app_name}}.apps.users import users


class DefaultConfig(object):
    DEBUG = True

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_NAME = "{{cookiecutter.app_name}}"
    SECRET_KEY = "PLEASE_CHANGE_ME"

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    STATIC_DIR = os.path.join(PROJECT_ROOT, '{{cookiecutter.app_name}}', 'apps', 'static')
    TEMPLATE_DIR = os.path.join(PROJECT_ROOT, '{{cookiecutter.app_name}}', 'apps', 'templates')

    BLUEPRINTS = (www, users)

    LOG_INI = 'etc/logging.ini.json'

    CONFIRMATION_TOKEN_SALT = "PLEASE_CHANGE_ME"

    # Flask-Mail
    MAIL_SERVER = "localhost"
    MAIL_PORT = "1025"
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEBUG = DEBUG
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = None
    MAIL_MAX_EMAILS = None
    MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = False

# vim: filetype=python
