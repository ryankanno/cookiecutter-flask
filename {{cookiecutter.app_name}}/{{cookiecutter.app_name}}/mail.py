#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template
from flask_mail import Message
from .extensions import mail
from structlog import get_logger

logger = get_logger()


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

    logger.debug("Sending email",
        subject=subject, sender=sender, recipients=recipients,
        plain_template_path=plain_template_path,
        html_template_path=html_template_path)

    mail.send(msg)

# vim: filetype=python
