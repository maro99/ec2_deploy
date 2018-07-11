from .base import *

EC2_DEPLOY = os.path.dirname(BASE_DIR)

SECRET_DIR =os.path.join(EC2_DEPLOY,'.secrets')
json_data = open(f'{SECRET_DIR}/dev.json').read()
data = json.loads(json_data)

DEBUG = True

DEFAULT_FILE_STORAGE = "config.storages.S3DefaultStorage"
STATICFILES_STORAGE = 'config.storages.S3StaticStorage'

AWS_ACCESS_KEY_ID =  data["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = data["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = data["AWS_STORAGE_BUCKET_NAME"]
AWS_DEFAULT_ACL =  data["AWS_DEFAULT_ACL"]
AWS_S3_REGION_NAME = data["AWS_S3_REGION_NAME"]
AWS_S3_SIGNATURE_VERSION = data["AWS_S3_SIGNATURE_VERSION"]


# Static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
MEDIA_ROOT = os.path.join(EC2_DEPLOY,'.media')
MEDIA_URL ='/media/'

# wsgi
WSGI_APPLICATION = 'config.wsgi.dev.application'

# DB
DATABASES = data["DATABASES"]

print(DATABASES)

# django-storages
INSTALLED_APPS +=[
    'storages',
]




print(data)


