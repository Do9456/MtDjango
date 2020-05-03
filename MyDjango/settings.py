"""
Django settings for MyDjango project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

#项目路径
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

#秘钥配置
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'az+&l6#ezh+577-z+zji(b$6#rp%fkm2)h@0&x&key8%ylux%$'

#调试模式
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#域名访问
#域名访问设置可以访问的域名列表，当 DEBUG 为 True 时，默认只能在本机浏览器访问调试；否则需要填写 ALLOWED_HOSTS，指定容许访问的域名。
ALLOWED_HOSTS = []

#APP列表
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'MyApp.apps.MyappConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',    #安全机制，保护通信安全
    'django.contrib.sessions.middleware.SessionMiddleware', #会话session功能
    'django.middleware.locale.LocaleMiddleware',  # 新增中间件，支持中文显示
    'django.middleware.common.CommonMiddleware',    #处理请求信息，规范请求内容
    'django.middleware.csrf.CsrfViewMiddleware',    #开启CSRF防护
    'django.contrib.auth.middleware.AuthenticationMiddleware',  #开启内置的用户认证
    'django.contrib.messages.middleware.MessageMiddleware', #开启信息提示功能
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   #防止恶意程序单机劫持
]

ROOT_URLCONF = 'MyDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'MyApp/templates')
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# 4 种数据库引擎
# 数据库postgresql
##'django.db.backends.postgresql'

# mysql数据库
##'django.db.backends.mysql'

# sqlite数据库
##'django.db.backends.sqlite3'

# oracle数据库
##'django.db.backends.oracle'

DATABASES = {
    ##默认sqlite库
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
##mysql连接配置
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django',    # 数据库名
            'USER': 'root',      # 登录用户名
            'PASSWORD': 'root',    # 登录密码
            'HOST': '127.0.0.1',  # 服务器地址
            'PORT': '3306',   # 数据库端口号，一般为：3306
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
#默认只能找到APP下的static下面的
STATIC_URL = '/static/'

# settings.py
# 静态资源集合
# 加入项目根目录下的static文件夹
# App下自定义的静态资源文件夹
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),
                    os.path.join(BASE_DIR, 'MyApp/static')]

# 三个静态文件目录下的静态文件都可以访问
# http://127.0.0.1:8000/static/1.png

## 资源部署
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
# 把静态文件收集到 STATIC_ROOT中。
# python3 manage.py collectstatic

# 媒体资源
# 设置媒体路由地址信息
MEDIA_URL = './media/'
# media文件夹的完整路径
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

