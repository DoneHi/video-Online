import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MYSQL_DB_SETTING = {
    'ENGINE': 'django.db.backends.mysql',
    'HOST': '127.0.0.1',
    'USER': 'root',
    'PASSWORD': '123456',
    'NAME': 'imooc',
}

SQLITE_DB_SETTING = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'iWaimai/../../db.sqlite3'),
}