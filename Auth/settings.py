"""
Django settings for Auth project.

Generated by 'django-admin startproject' using Django 1.11.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a)#3uvq)=1j=%ds3x6tqp##k#9^4m*4flif74j=4zglzt^xiq5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01.apps.App01Config',
    #第一步，添加到app配置项目下
    # 'debug_toolbar'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #第三步 中间件中配置中间件
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'Auth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Auth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bbs',
        'HOST':'127.0.0.1',
        'PORT':3306,
        'USER':'root',
        'PASSWORD':''
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]

LOGIN_URL='/login/'

AUTH_USER_MODEL = "app01.UserInfo"

#用户上传的文件的配置项
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')


# 记录日志功能
# BASE_LOG_DIR=os.path.join(BASE_DIR,'log')
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'standard': {
#             'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
#                       '[%(levelname)s][%(message)s]'
#         },
#         'simple': {
#             'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
#         },
#         'collect': {
#             'format': '%(message)s'
#         }
#     },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'default': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#             'filename': os.path.join(BASE_LOG_DIR, "xxx_info.log"),  # 日志文件
#             'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
#             'backupCount': 3,
#             'formatter': 'standard',
#             'encoding': 'utf-8',
#         },
#         'error': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#             'filename': os.path.join(BASE_LOG_DIR, "xxx_err.log"),  # 日志文件
#             'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
#             'backupCount': 5,
#             'formatter': 'standard',
#             'encoding': 'utf-8',
#         },
#         'collect': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#             'filename': os.path.join(BASE_LOG_DIR, "xxx_collect.log"),
#             'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
#             'backupCount': 5,
#             'formatter': 'collect',
#             'encoding': "utf-8"
#         }
#     },
#     'loggers': {
#        # 默认的logger应用如下配置
#         '': {
#             'handlers': ['default', 'error'],  # 上线之后可以把'console'移除
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         # 名为 'collect'的logger还单独处理
#         'collect': {
#             'handlers': ['console', 'collect'],
#             'level': 'INFO',
#         }
#     },
# }

#第四步，如果是本机调试，还需要将127.0.0.1加入到INTERNAL_IPS配置项中
# INTERNAL_IPS = ['127.0.0.1',]









