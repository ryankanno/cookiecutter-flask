#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask.ext.login import current_user
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask.ext.login import logout_user

from {{cookiecutter.app_name}}.extensions import login_manager
from .decorators import anonymous_user_required
from .forms import LoginForm
from .forms import RegisterForm
from .models import User
from .registerable import register_user
from werkzeug.datastructures import MultiDict

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/confirm_email', methods=['GET'])
def confirm_email():
    return redirect('/')


@users.route('/forgot_password', methods=['GET', 'POST'])
@anonymous_user_required
def forgot_password():
    if request.json:
        form = ForgotPasswordForm(MultiDict(request.json))
    else:
        form = ForgotPasswordForm()

    if form.validate_on_submit():
        send_reset_password_instructions(form.user)

    if request.json:
        return _render_json(form)

    return render_template('users/forgot_password.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(MultiDict(request.json)) if request.json else LoginForm()

    if form.validate_on_submit():
        login_user(form.user, remember=form.remember.data)

        if not request.json:
            return redirect(url_for('www.slash'))

    if request.json:
        return _render_json(form)
    else:
        return render_template('users/login.html', form=form)


def _render_json(form):

    if len(form.errors) > 0:
        code = 400
        response = dict(errors=form.errors)
    else:
        code = 200
        response = {}
        response['user'] = dict(id=str(form.user.id))
        response['user']['authentication_token'] = form.user.get_auth_token()

    return jsonify(dict(meta=dict(code=code), response=response))


@users.route('/logout')
@login_required
def logout():
    if current_user.is_authenticated():
        logout_user()

    return redirect(request.args.get('next', None) or
                    url_for('www.slash'))


@users.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = register_user(**form.data)
        login_user(user)
        return redirect(url_for('www.slash'))
    return render_template('users/register.html', form=form)


@login_manager.user_loader
def load_user(userid):
    return User.get(userid)

# vim: filetype=python
