.. _documentation:

Documentation
*************

`Full documentation <https://django-markdowny.readthedocs.io/>`_ is available online.

However, you can also build the documentation from source. Enter your `virtual environment <https://docs.python.org/3/library/venv.html>`_.

.. code-block:: bash

   $ source myvenv/bin/activate

Clone the code repository.

.. code-block:: bash

   (myvenv)$ git clone git@github.com:richardcornish/django-markdowny.git
   (myvenv)$ cd django-markdowny/

Install `Sphinx <http://www.sphinx-doc.org/>`_, |sphinx-autobuild|_, and |sphinx_rtd_theme|_.

.. |sphinx-autobuild| replace:: ``sphinx-autobuild``
.. _sphinx-autobuild: https://pypi.python.org/pypi/sphinx-autobuild

.. |sphinx_rtd_theme| replace:: ``sphinx_rtd_theme``
.. _sphinx_rtd_theme: https://pypi.python.org/pypi/sphinx_rtd_theme

.. code-block:: bash

   (myvenv)$ pip install sphinx sphinx-autobuild sphinx_rtd_theme

Create an HTML build.

.. code-block:: bash

   (myvenv)$ (cd docs/ && make html)

Or use ``sphinx-autobuild`` to watch for live changes.

.. code-block:: bash

   (myvenv)$ sphinx-autobuild docs/ docs/_build_html

Open `127.0.0.1:8000 <http://127.0.0.1:8000>`_.
