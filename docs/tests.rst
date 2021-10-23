.. _tests:

Tests
*****

`Continuous integration test results <https://app.travis-ci.com/github/richardcornish/django-markdowny>`_ are available online.

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
