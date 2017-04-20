Django Markdownify
******************

|PyPI version|_ |Build status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-markdownify.svg
.. _PyPI version: https://pypi.python.org/pypi/django-markdownify

.. |Build status| image::
   https://travis-ci.org/richardcornish/django-markdownify.svg?branch=master
.. _Build status: https://travis-ci.org/richardcornish/django-markdownify

**Django Markdownify** is a `Django <https://www.djangoproject.com/>`_ `template tag <https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/>`_ application to convert `Markdown <http://daringfireball.net/projects/markdown/>`_ to HTML.

Unlike other Django/Markdown filters, Markdownify supports all of the options available in `Python Markdown <https://pythonhosted.org/Markdown/reference.html>`_ via settings.

* `Package distribution <https://pypi.python.org/pypi/django-markdownify>`_
* `Code repository <https://github.com/richardcornish/django-markdownify>`_
* `Documentation <https://django-markdownify.readthedocs.io/>`_
* `Tests <https://travis-ci.org/richardcornish/django-markdownify>`_

Install
=======

.. code-block:: bash

   $ pip install django-markdownify

Add to ``settings.py``.

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       'markdownify',
   ]

Usage
=====

.. code-block:: django

   {% load markdownify_tags %}

   {% markdownify %}
   # Hello, world!
   {% endmarkdownify %}

Result:

.. code-block:: html

   <h1>Hello, world!</h1>
