.. _tests:

Tests
*****

`Continuous integration test results <https://travis-ci.org/richardcornish/django-markdowny>`_ are available online.

However, you can also test the source code.

.. code-block:: bash

   $ workon myvenv
   (myvenv)$ django-admin test markdowny.tests --settings="markdowny.tests.settings"
   
   System check identified no issues (0 silenced).
   ............
   ----------------------------------------------------------------------
   Ran 12 tests in 0.154s
   
   OK
   Destroying test database for alias 'default'...

A bundled settings file allows you to test the code without even creating a Django project.
