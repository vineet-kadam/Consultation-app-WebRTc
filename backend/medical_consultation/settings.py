"""
medical_consultation/settings.py
"""

from datetime import timedelta
from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-your-secret-key-here")

DEBUG = True


ALLOWED_HOSTS = ['192.168.0.104','192.168.10.191', '127.0.0.1', 'localhost']
INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "channels",
    "consultation",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "medical_consultation.urls"

CORS_ALLOW_ALL_ORIGINS = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "medical_consultation.wsgi.application"
ASGI_APPLICATION  = "medical_consultation.asgi.application"

# -- Database Configuration ----------------------------------------------------
DATABASE_TYPE = os.getenv("DATABASE_TYPE", "sqlite").lower()

if DATABASE_TYPE == "postgres":
    DATABASES = {
        "default": {
            "ENGINE"  : "django.db.backends.postgresql",
            "NAME"    : os.getenv("DB_NAME", "medical_consultation_db"),
            "USER"    : os.getenv("DB_USER", "postgres"),
            "PASSWORD": os.getenv("DB_PASSWORD", "Mit@1724"),
            "HOST"    : os.getenv("DB_HOST", "127.0.0.1"),
            "PORT"    : os.getenv("DB_PORT", "5432"),
        }
    }
else:
    # Default to SQLite for ease of development and resilience
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
            "OPTIONS": {
                "timeout": 20,  # Helps prevent "database is locked" errors
            },
        }
    }

AUTH_USER_MODEL = 'consultation.User'

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = 'Asia/Kolkata'
USE_I18N      = True
USE_TZ        = True

STATIC_URL = "static/"
MEDIA_URL  = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -- Django Channels -----------------------------------------------------------
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

# -- DRF + JWT -----------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME" : timedelta(hours=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# Deepgram API key (Loaded from .env or environment variable)
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY", "241891d132965abc6b1488661f56229bc0d70f47")

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://192.168.0.104:3000",
    "http://192.168.10.191:8000"
]

API = "localhost:3000"