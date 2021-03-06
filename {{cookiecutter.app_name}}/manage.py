#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from flask.ext.script import prompt_bool
from flask.ext.migrate import Migrate
from flask.ext.migrate import MigrateCommand
from {{cookiecutter.app_name}}.app import get_app
from {{cookiecutter.app_name}}.extensions import db

app = get_app()

# initialize flask-migrate
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.option('-h', '--host', dest='host', default='127.0.0.1')
@manager.option('-p', '--port', dest='port', type=int, default=5000)
@manager.option('-w', '--workers', dest='workers', type=int, default=3)
def gunicorn(host, port, workers):
    """Start the Server with Gunicorn"""
    from gunicorn.app.base import Application

    class FlaskApplication(Application):
        def init(self, parser, opts, args):
            return {
                'bind': '{0}:{1}'.format(host, port),
                'workers': workers
            }

        def load(self):
            return app

    application = FlaskApplication()
    return application.run()


@manager.command
def createdb():
    """
    Creates all database tables
    """
    db.create_all()


@manager.command
def dropdb(force=False):
    """
    Drops all database tables
    """

    if force or prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()


if __name__ == "__main__":
    manager.run()

# vim: filetype=python
