from django.conf import settings


MARKDOWNY = {
    "extensions": [],
    "extension_configs": {},
    "output_format": "html",
    "tab_length": 4,
}

user_settings = getattr(settings, "MARKDOWNY", {})

MARKDOWNY.update(user_settings)
