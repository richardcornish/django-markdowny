.. _settings:

Settings
********

The template tag offers one setting that nests options as a dictionary. By default, it is:

.. code-block:: python

   MARKDOWNY = {
       'extensions': [],
       'extension_configs': {},
       'output_format': 'html',
       'tab_length': 4,
   }

The keys of the dictionary correspond to the keyword arguments of Python-Markdown's |markdown|_ method, which means you're free to use any of several options, such as ``extensions`` or ``output_format``. Opinionated default options include:

.. |Markdown| replace:: ``markdown``
.. _Markdown: https://python-markdown.github.io/reference/#markdown

* ``output_format`` is a string indicating the version of HTML to output. Python-Markdown sets ``xhtml`` by default. ``xhtml`` is replaced by ``html``.

The other options are reproduced from Python-Markdown's existing defaults for the purpose of aiding in "fallback" values when resolving non-existent template variables acting as keyword arguments in the template tag.

A more customized example might look like:

.. code-block:: python

   MARKDOWNY = {
       'extensions': [
           'abbr',
           'footnotes',
       ],
       'extension_configs': {
           'footnotes': {
               'PLACE_MARKER': '/Footnotes Go Here/',
           }
       },
       'output_format': 'xhtml',
       'tab_length': 2,
   }

See Python-Markdown documentation for all `officially supported extensions <https://python-markdown.github.io/extensions/>`_.

This setting is also available on a per-template basis. See examples in :ref:`Usage` for details.
