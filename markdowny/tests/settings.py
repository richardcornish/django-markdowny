import os


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "fake-key"

INSTALLED_APPS = [
    "markdowny",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "TEST": {
            "NAME": None,
        },
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
    }
]
