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

   {% markdowny %}Hello, world!{% endmarkdowny %}

Or use it as a template filter.

.. code-block:: django

   {{ post.body|markdowny }}

Result:

.. code-block:: html

   <p>Hello, world!</p>

Customize with keyword arguments
================================

Additionally customize the behavior of the ``{% markdowny %}`` tag with keyword arguments that correspond to those of Python-Markdown's |markdown|_ method.

.. code-block:: django

   {% markdowny output_format='xhtml' tab_length=2 %}Hello, world!{% endmarkdowny %}

At the time of this writing, arguments include:

* ``extensions``
* ``extension_configs``
* ``output_format``
* ``tab_length``

Django's template language `cannot interpret native Python code <https://docs.djangoproject.com/en/dev/ref/templates/language/>`_. However, keyword arguments in template tags can declaratively accept strings and numbers; that is, when specifying ``output_format`` and/or ``tab_length``, their values--`'xhtml'` and `2` in the prior example, respectively--can be assigned upon declaration. The other keyword arguments--``extensions`` and ``extension_configs``--cannot accept a declarative assignment because |markdown|_ expects a native Python list and dictionary, respectively.

Therefore, if specifying ``extensions`` and/or ``extension_configs`` in the template tag, their values should be made available by the template context. For example, if one wanted ``extensions`` declared in the template tag and ``my_extensions`` existed in the template context:

.. code-block:: django

   {% markdowny extensions=my_extensions %}Hello, world!{% endmarkdowny %}

The view (or middleware, context processor, etc.) should then make ``my_extensions`` available.

.. code-block:: python

   from django.shortcuts import render

   def my_view(request):
       return render(request, 'my_template.html', context={
           'my_extensions': ['abbr'],
       })

Likewise for ``extension_configs`` and its expectation of a dictionary. Like ``extensions`` and ``extension_configs``, the ``output_format`` and ``tab_length`` keyword arguments can also accept template variables as their values should you choose.

.. code-block:: django

   {% markdowny output_format=my_output_format tab_length=my_tab_length %}Hello, world!{% endmarkdowny %}

If a required template variable does not exist in the context, then its value from the project's settings will be used, falling back to the default app :ref:`Settings` as a last resort.

.. warning::
    Previous versions of the template tag expected keyword arguments as strings mimicking the appearance of native Python types; e.g., ``{% markdowny extensions='["abbr"]' %}Hello, world!{% endmarkdowny %}``. This is always a bad idea, and the behavior has since been removed.

.. |Markdown| replace:: ``Markdown``
.. _Markdown: https://python-markdown.github.io/reference/#markdown
