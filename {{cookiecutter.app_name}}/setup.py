#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


HERE = os.path.dirname(os.path.realpath(__file__))


with open(os.path.join(HERE, 'README.rst')) as readme_file:
    readme = readme_file.read()


with open(os.path.join(HERE, 'HISTORY.rst')) as history_file:
    history = history_file.read().replace('.. :changelog:', '')

# Metadata

meta = {}
re_meta = re.compile(r'__(\w+?)__\s*=\s*(.*)')
re_version = re.compile(r'VERSION\s*=.*?\((.*?)\)')
strip_quotes = lambda s: s.strip("\"'")


def add_version(match):
    return {'VERSION': match.group(1).replace(" ", "").replace(",", ".")}


def add_meta(match):
    attr_name, attr_value = m.groups()
    return {attr_name: strip_quotes(attr_value)}


patterns = {
    re_meta: add_meta,
    re_version: add_version
}


relative_init_path = '{{ cookiecutter.app_name }}/__init__.py'
with open(os.path.join(HERE, relative_init_path), 'r') as f:
    for line in f:
        for pattern, handler in patterns.items():
            m = pattern.match(line.strip())
            if m:
                meta.update(handler(m))

# Requires

requires = [
    'Flask==0.10.1',
    'Flask-Bcrypt',
    'Flask-Cache',
    'Flask-Login',
    'Flask-Mail',
    'Flask-SeaSurf',
    'Flask-Security',
    'Flask-Script',
    'Flask-DebugToolbar'
]
tests_require = ['pytest']
classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    "Programming Language :: Python :: 2",
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
]

setup(
    name='{{ cookiecutter.project_name }}',
    version=meta['VERSION'],
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + history,
    author=meta['author'],
    author_email=meta['email'],
    url='{{ cookiecutter.project_url }}',
    packages=[
        '{{ cookiecutter.app_name }}',
    ],
    package_dir={'{{ cookiecutter.app_name }}':
                 '{{ cookiecutter.app_name }}'},
    include_package_data=True,
    install_requires=requires,
    license=meta['license'],
    zip_safe=False,
    keywords='{{ cookiecutter.app_name }}',
    classifiers=classifiers,
    test_suite='tests',
    tests_require=tests_require,
)

# vim: filetype=python
