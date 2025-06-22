# settings.py — Student Project
# (تم التعديل ليدعم كلًّا من بيئة التطوير وبيئة النشر على Render)

from pathlib import Path
import os
import cloudinary
import dj_database_url   # ➕ لتحليل رابط قاعدة البيانات في بيئة النشر

# ────────────────────────────────────────────────
# المسارات الأساسية
# ────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ────────────────────────────────────────────────
# مفاتيح الأمان
# ────────────────────────────────────────────────
# تأكد من وضع هذه القيم في متغيرات بيئة عند النشر
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    'django-insecure-01k1y(b-dej2tt2sh3tk_6o547ep)x()fi4ioxg*o=ic13l*uw'
)

DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"

# السماح للدومينات في الإنتاج (يُضبط عبر متغير بيئة)
ALLOWED_HOSTS: list[str] = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",") if not DEBUG else []

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
# افتراضيًا SQLite لبيئة التطوير
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# عند وجود متغير DATABASE_URL (مثل Render) ➜ استخدم PostgreSQL
if os.getenv("DATABASE_URL"):
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600,
        ssl_require=True
    )

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
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # مجلد التجميع في الإنتاج

# ────────────────────────────────────────────────
# Cloudinary Storage
# ────────────────────────────────────────────────
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME', 'da4etlrox'),
    'API_KEY':    os.getenv('CLOUDINARY_API_KEY',    '591474588512373'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET', 'DsvPexFFqmhS5Sm7A7Mj-w_6BUU'),
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
# ملفات الوسائط
# ────────────────────────────────────────────────
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
