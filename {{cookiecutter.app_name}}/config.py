#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
from os import environ as env
from {{cookiecutter.app_name}}.apps.www import www
from {{cookiecutter.app_name}}.apps.users import users


def as_bool(key, default):
    return env.get(key, str(default)).lower() \
        in ("yes", "true", "t", "1")


class DefaultConfig(object):

    DEBUG = as_bool('DEBUG', True)

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_NAME = "{{cookiecutter.app_name}}"
    SECRET_KEY = env.get('SECRET_KEY', 'PLEASE_CHANGE_ME')

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    DEBUG_TB_INTERCEPT_REDIRECTS = as_bool('DEBUG_TB_INTERCEPT_REDIRECTS',
                                           False)

    STATIC_DIR = os.path.join(PROJECT_ROOT, '{{cookiecutter.app_name}}', 'apps', 'static')
    TEMPLATE_DIR = os.path.join(PROJECT_ROOT, '{{cookiecutter.app_name}}', 'apps', 'templates')

    BLUEPRINTS = (www, users)

    LOG_INI = 'etc/logging.ini.json'

    # Users Register / Login
    USERS_CONFIRMATION_REQUIRED = \
        as_bool('USERS_CONFIRMATION_REQUIRED', True)
    USERS_REGISTER_CONFIRMATION_TOKEN_MAX_AGE_IN_SECONDS = \
        env.get('USERS_REGISTER CONFIRMATION_TOKEN_MAX_AGE_IN_SECONDS', 604800)
    USERS_REGISTER_CONFIRMATION_TOKEN_SALT = \
        env.get('USERS_REGISTER CONFIRMATION_TOKEN_SALT', 'PLEASE_CHANGE_ME')
    USERS_RESET_PASSWORD_TOKEN_MAX_AGE_IN_SECONDS = \
        env.get('USERS_RESET_PASSWORD_TOKEN_MAX_AGE_IN_SECONDS', 604800)
    USERS_RESET_PASSWORD_TOKEN_SALT = \
        env.get('USERS_RESET_PASSWORD_TOKEN_SALT ', 'PLEASE_CHANGE_ME')

    # Flask-Mail
    MAIL_SERVER = env.get('MAIL_SERVER,', 'localhost')
    MAIL_PORT = env.get('MAIL_PORT,', '1025')
    MAIL_USE_TLS = as_bool('MAIL_USE_TLS', False)
    MAIL_USE_SSL = as_bool('MAIL_USE_SSL', False)
    MAIL_DEBUG = DEBUG
    MAIL_USERNAME = env.get('MAIL_USERNAME', None)
    MAIL_PASSWORD = env.get('MAIL_PASSWORD', None)
    MAIL_DEFAULT_SENDER = env.get('MAIL_DEFAULT_SENDER', None)
    MAIL_MAX_EMAILS = env.get('MAIL_MAX_EMAILS', None)
    MAIL_SUPPRESS_SEND = as_bool('MAIL_USE_SSL', False)
    MAIL_ASCII_ATTACHMENTS = as_bool('MAIL_USE_SSL', False)

    # Flask-Login
    REMEBER_COOKIE_DURATION = datetime.timedelta(days=7)

# vim: filetype=python
