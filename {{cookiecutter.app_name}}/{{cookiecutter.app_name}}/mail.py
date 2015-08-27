#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template
from flask_mail import Message
from .extensions import mail
import logging


def send_mail(
        subject,
        sender,
        recipients,
        plain_template_path=None,
        html_template_path=None,
        **context):

    if type(recipients) is not list:
        recipients = [recipients]

    msg = Message(subject,
                  sender=sender,
                  recipients=recipients)

    if plain_template_path:
        msg.body = render_template(plain_template_path, **context)

    if html_template_path:
        msg.html = render_template(html_template_path, **context)

    logging.debug("Sending email from {0} to {1} recipients"
        .format(sender, len(recipients)))

    mail.send(msg)

# vim: filetype=python
