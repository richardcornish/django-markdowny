.. _install:

Install
*******

Install with the `pip <https://pip.pypa.io/en/stable/>`_ package manager.

.. code-block:: bash

   $ python -m venv myvenv
   $ source myvenv/bin/activate
   (myvenv)$ pip install django
   (myvenv)$ pip install django-markdowny

After `creating a project <https://docs.djangoproject.com/en/dev/intro/tutorial01/>`_, add ``markdowny`` to ``INSTALLED_APPS`` in ``settings.py``.

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       'markdowny',
   ]

Remember to update your ``requirements.txt`` file. In your project directory:

.. code-block:: bash

   (myvenv)$ pip freeze > requirements.txt
