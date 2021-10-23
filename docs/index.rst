.. _index:
.. module:: markdowny

Django Markdowny
****************

|PyPI version|_ |Build status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-markdowny.svg
.. _PyPI version: https://pypi.org/project/django-markdowny/

.. |Build status| image::
   https://api.travis-ci.com/richardcornish/django-markdowny.svg?branch=main
.. _Build status: https://app.travis-ci.com/github/richardcornish/django-markdowny

**Django Markdowny** is a `Django <https://www.djangoproject.com/>`_ `template tag <https://docs.djangoproject.com/en/dev/howto/custom-template-tags/>`_ application to convert `Markdown <https://daringfireball.net/projects/markdown/>`_ into HTML with `Python-Markdown <https://python-markdown.github.io/>`_.

Unlike other Django-Markdown filters, Markdowny supports `all of the options <https://python-markdown.github.io/reference/>`_ in Python-Markdown via :ref:`Settings`.

* `Package <https://pypi.org/project/django-markdowny/>`_
* `Source <https://github.com/richardcornish/django-markdowny>`_
* `Documentation <https://django-markdowny.readthedocs.io/>`_
* `Tests <https://app.travis-ci.com/github/richardcornish/django-markdowny>`_

Install
=======

.. code-block:: bash

   $ pip install django-markdowny

Add to ``settings.py``.

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       'markdowny',
   ]

Usage
=====

Use as a template tag.

.. code-block:: django

   {% load markdowny_tags %}

   {% markdowny %}Hello, world!{% endmarkdowny %}

Or as a template filter.

.. code-block:: django

   {{ post.body|markdowny }}

Result:

.. code-block:: html

   <p>Hello, world!</p>

Contents
========

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install
   usage
   settings
   documentation
   tests


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
