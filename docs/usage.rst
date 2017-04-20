.. _usage:

Usage
*****

HTML
====

Load the template tags.

.. code-block:: django

   {% load markdowny_tags %}

Use the ``{% markdowny %}`` template tag to convert Markdown into HTML.

.. code-block:: django

   {% markdowny %}
   # Hello, world!
   {% endmarkdowny %}

Result:

.. code-block:: html

   <h1>Hello, world!</h1>

Customize with keyword arguments
================================

Additionally customize the behavior of the ``{% markdowny %}`` tag with keyword arguments that correspond to all available options of Python Markdown's |Markdown|_ class, such as ``extensions`` and ``output_format``, as keyword arguments.

.. code-block:: django

   {% markdowny extensions='["abbr", "codehilite"]' output_format='xhtml1' lazy_ol='true' %}
   # Hello, world!
   {% endmarkdowny %}

Because Django's template language is not Python, template tags expect either a string or a number as a keyword argument. Therefore, in instances when Python Markdown's ``Markdown`` constructor expects a Python data type, such as a string, number, boolean, or list, the value of the keyword argument should be the equivalent string or number. For example, pass ``'true'`` as the equivalent of ``True`` or ``'[...]'`` as the equivalent of ``[...]``. Numbers can be left as is. All keyword arguments are later coerced into Python data types.

See Python Markdown's documentation on the |Markdown|_ class for all available keyword arguments.

.. |Markdown| replace:: ``Markdown``
.. _Markdown: https://pythonhosted.org/Markdown/reference.html#markdown
