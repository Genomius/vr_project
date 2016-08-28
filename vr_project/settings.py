import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'b&5uc@#sp6uczbp70yv2usa_qv!#4f*=m$k)k-^l(k8qhsi_^7'
DEBUG = True
ALLOWED_HOSTS = []

DOMAIN_NAME = "VR55.ru"

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'main',
    'catalog',
    'cart',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vr_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'vr_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'files', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

GRAPPELLI_ADMIN_TITLE = 'VRproject'
GRAPPELLI_INDEX_DASHBOARD = 'vr_project.dashboard.CustomIndexDashboard'

email_from = "denis.baylo@gmail.com"

MAIL_USE_TLS = False
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'denis.baylo@gmail.com'
SERVER_EMAIL = 'denis.baylo@gmail.com'
EMAIL_HOST_PASSWORD = 'denisdenis688192'
EMAIL_SUBJECT_PREFIX = '[VR55]'
DEFAULT_FROM_EMAIL = 'denis.baylo@gmail.com'