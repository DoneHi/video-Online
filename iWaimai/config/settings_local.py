import os

from .settings_db import SQLITE_DB_SETTING

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': SQLITE_DB_SETTING
}

ALLOWED_HOSTS = ['*']

EMAIL_HOST = 'smtp.sina.cn'
EMAIL_PORT = 25
EMAIL_HOST_USER = '13358873548@sina.cn'
EMAIL_HOST_PASSWORD = '13945657337xX'
EMAIL_USE_TLS = False
EMAIL_FROM = '13358873548@sina.cn'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]