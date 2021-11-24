Django Markdowny
****************

|PyPI version|_ |Build status|_ |Documentation status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-markdowny.svg
.. _PyPI version: https://pypi.org/project/django-markdowny/

.. |Build status| image::
   https://github.com/richardcornish/django-markdowny/actions/workflows/main.yml/badge.svg
.. _Build status: https://github.com/richardcornish/django-markdowny/actions/workflows/main.yml

.. |Documentation status| image::
   https://readthedocs.org/projects/django-markdowny/badge/?version=latest
.. _Documentation status: https://django-markdowny.readthedocs.io/en/latest/?badge=latest

**Django Markdowny** is a `Django <https://www.djangoproject.com/>`_ `template tag <https://docs.djangoproject.com/en/dev/howto/custom-template-tags/>`_ application to convert `Markdown <https://daringfireball.net/projects/markdown/>`_ into HTML with `Python-Markdown <https://python-markdown.github.io/>`_.

Unlike other Django-Markdown filters, Markdowny supports `all of the options <https://python-markdown.github.io/reference/>`_ in Python-Markdown via `settings <https://django-markdowny.readthedocs.io/en/latest/settings.html>`_.

* `Package <https://pypi.org/project/django-markdowny/>`_
* `Source <https://github.com/richardcornish/django-markdowny>`_
* `Documentation <https://django-markdowny.readthedocs.io/>`_
* `Tests <https://github.com/richardcornish/django-markdowny/actions/workflows/main.yml>`_

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

   {{ 'Hello, world!'|markdowny }}

Result:

.. code-block:: html

   <p>Hello, world!</p>
