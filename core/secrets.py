DJANGO_SECRET_KEY = 'django-insecure-3ozp-6)klpsx-3gz3-1v6$o8l=gn4k#l7ho48r@#3cn!u=ncdv'

Default_Database_Configuration = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ezypzy',
        'USER': 'postgres',
        'PASSWORD': 'Malik@0900',
        'HOST': 'localhost',
        'PORT': '5432',
    }

# Set your AWS credentials and bucket name
AWS_ACCESS_KEY_ID = 'AKIAVPZ7YJIGW443UCMQ'
AWS_SECRET_ACCESS_KEY = 'pBH6Ca6F6KhA1xX8K3fKxJvx/UIBfm8zpNwbIKFk'
AWS_STORAGE_BUCKET_NAME = 'pdfezypzy'
AWS_S3_REGION_NAME = 'ap-south-1'  # Change to your desired region
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
# Use Amazon S3 for static and media files
AWS_S3_CUSTOM_DOMAIN = 'ezypzy-n73d3xtbr4ykrdspt5r779cb46fd4aps3a-s3alias.s3.ap-south-1.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  # Cache files for a day
}

# Use S3 for static files
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Use S3 for media files
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'