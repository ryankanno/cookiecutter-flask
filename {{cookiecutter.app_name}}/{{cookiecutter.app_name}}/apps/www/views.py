#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template
from {{cookiecutter.app_name}}.apps.users.forms import LoginForm


www = Blueprint('www', __name__, template_folder='templates')


@www.route('/')
def slash():
    return render_template('www/slash.html')

# vim: filetype=python
