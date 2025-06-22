from pathlib import Path
import os
import cloudinary

# ────────────────────────────────────────────────
# المسارات الأساسية
# ────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ ضع هذا المفتاح في متغير بيئة عند نشر المشروع
SECRET_KEY = 'django-insecure-01k1y(b-dej2tt2sh3tk_6o547ep)x()fi4ioxg*o=ic13l*uw'

DEBUG = True
ALLOWED_HOSTS: list[str] = []

# ────────────────────────────────────────────────
# التطبيقات
# ────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ تطبيقات المشروع
    'accounts',
    'courses',
    'enrollments',

    # ✅ Cloudinary
    'cloudinary',
    'cloudinary_storage',
]

# ────────────────────────────────────────────────
# الوسطاء
# ────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Student.urls'

# ────────────────────────────────────────────────
# القوالب
# ────────────────────────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Student.wsgi.application'

# ────────────────────────────────────────────────
# قاعدة البيانات
# ────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ────────────────────────────────────────────────
# التحقق من كلمات المرور
# ────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ────────────────────────────────────────────────
# اللغة والتوقيت
# ────────────────────────────────────────────────
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# ────────────────────────────────────────────────
# الملفات الثابتة
# ────────────────────────────────────────────────
STATIC_URL = 'static/'

# ────────────────────────────────────────────────
# Cloudinary Storage
# ────────────────────────────────────────────────
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'da4etlrox',
    'API_KEY':    '591474588512373',
    'API_SECRET': 'DsvPexFFqmhS5Sm7A7Mj-w_6BUU',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# تهيئة Cloudinary لاستخدامها في shell وأي كود Python
cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=CLOUDINARY_STORAGE['API_KEY'],
    api_secret=CLOUDINARY_STORAGE['API_SECRET'],
    secure=True
)

# ────────────────────────────────────────────────
# ملفات الوسائط (اختياري أثناء التطوير)
# ────────────────────────────────────────────────
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
