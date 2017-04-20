from __future__ import unicode_literals

import ast

from markdown import markdown


def bits_to_dict(bits):
    """Convert a template tag's kwargs into a dictionary of Python types."""
    # Strip stray commas
    cleaned_bits = [bit[:-1] if bit.endswith(',') else bit for bit in bits]

    # Split on equals sign to create dictionary
    options = dict(bit.split('=') for bit in cleaned_bits)

    # Convert to Python types
    for key in options:
        if options[key] == "'true'" or options[key] == "'false'":
            options[key] = options[key].title()
        options[key] = ast.literal_eval(options[key])

    return options


def markdownify(value, **kwargs):
    options = kwargs.get('options', {})
    return markdown(value, **options)
