.. _settings:

Settings
********

The template tag offers one setting that nests options as a dictionary. By default, it is:

.. code-block:: python

   MARKDOWNY = {
       'output_format': 'html5',
       'lazy_ol': False,
   }

The keys of the dictionary correspond to the keyword argument options of Python Markdown's |Markdown|_, which means you're free to use any of several options, such as ``extensions`` or ``output_format``. Python Markdown faithfully reproduces Markdown, almost slavishly so. Two opinionated default options include:

.. |Markdown| replace:: ``Markdown``
.. _Markdown: https://pythonhosted.org/Markdown/reference.html#markdown

* ``output_format`` is a string indicating the version of HTML to output. Python Markdown sets ``xhtml1`` by default. ``xhtml1`` is replaced by ``html5``.
* ``lazy_ol`` is a boolean indicating whether ordered lists should start at the number in the Markdown code. Python Markdown sets ``True`` by default, which always starts ordered lists at ``1``. ``True`` is replaced by ``False``.

A more customized example might look like:

.. code-block:: python

   MARKDOWNY = {
       'extensions': [
           'abbr',
           'codehilite',
           'fenced_code',
           'sane_lists',
           'smart_strong',
       ],
       'extension_configs': {},
       'output_format': 'xhtml1',
       'tab_length': 4,
       'smart_emphasis': True,
       'lazy_ol': True,
   }

See Python Markdown documentation for all `officially supported extensions <https://pythonhosted.org/Markdown/extensions/index.html>`_.

This setting is also available on a per-template basis. See examples in :ref:`Usage` for details.
