.. _tests:

Tests
*****

`Continuous integration test results <https://github.com/richardcornish/django-markdowny/actions/workflows/main.yml>`_ are available online.

However, you can also test the source code.

.. code-block:: bash

   $ source myvenv/bin/activate
   (myvenv)$ django-admin test markdowny.tests --settings="markdowny.tests.settings"
   Creating test database for alias 'default'...
   System check identified no issues (0 silenced).
   ..............
   ----------------------------------------------------------------------
   Ran 14 tests in 0.120s
   
   OK
   Destroying test database for alias 'default'...

A bundled settings file allows you to test the code without even creating a Django project.

You can also test against all currently supported versions of `Python <https://docs.djangoproject.com/en/dev/faq/install/#what-python-version-can-i-use-with-django>`_ and `Django <https://www.djangoproject.com/download/#supported-versions>`_ locally with `Tox <https://tox.wiki/>`_. Requires all necessary versions of Python installed locally.

.. code-block:: bash

   $ source myvenv/bin/activate
   (myvenv)$ pip install tox
   (myvenv)$ tox
   GLOB sdist-make: /path/to/django-markdowny/setup.py
   # ...
   ____________ summary ____________
   py36-django22: commands succeeded
   py37-django22: commands succeeded
   py38-django22: commands succeeded
   py39-django22: commands succeeded
   py36-django32: commands succeeded
   py37-django32: commands succeeded
   py38-django32: commands succeeded
   py39-django32: commands succeeded
   py310-django32: commands succeeded
   py38-django40: commands succeeded
   py39-django40: commands succeeded
   py310-django40: commands succeeded
   congratulations :)
