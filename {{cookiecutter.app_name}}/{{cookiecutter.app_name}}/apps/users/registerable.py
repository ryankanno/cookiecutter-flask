#!/usr/bin/env python
# -*- coding: utf-8 -*-

from {{cookiecutter.app_name}}.mail import send_mail
from .models import User
from .signals import user_registered
from .confirmable import generate_confirmation_token_and_link


def register_user(**kwargs):
    kwargs.pop('confirm', None)
    user = User.create(**kwargs)

    confirmation_token, confirmation_link = \
        generate_confirmation_token_and_link(user)

    user_registered.send(
        user=user,
        confirmation_token=confirmation_token)

    send_mail(
        'Thank you for registering!',
        current_app.config['MAIL_DEFAULT_SENDER'],
        user.email,
        plain_template_path='users/emails/welcome.txt',
        html_template_path='users/emails/welcome.html',
        user=user,
        confirmation_link=confirmation_link)

    return user

# vim: filetype=python
