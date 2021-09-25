from markdown import markdown as _markdown


def markdown(text, **kwargs):
    return _markdown(text, **kwargs)
