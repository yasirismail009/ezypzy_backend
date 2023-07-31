import os
import boto3
from storages.backends.s3boto3 import S3Boto3Storage
from core import secrets


AWS_ACCESS_KEY_ID = secrets.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = secrets.AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = secrets.AWS_STORAGE_BUCKET_NAME
AWS_S3_REGION_NAME = secrets.AWS_S3_REGION_NAME
AWS_S3_CUSTOM_DOMAIN = f'{secrets.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = 'public-read'  # Optional: Set the ACL for uploaded files
AWS_QUERYSTRING_AUTH = False     # Optional: Remove querystring authentication
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  # Optional: Set caching for uploaded files
}

# Custom storage classes for static and media files
class S3MediaStorage(S3Boto3Storage):
    location = 'media'  # Set the location for uploaded media files

class S3StaticStorage(S3Boto3Storage):
    location = 'static'  # Set the location for uploaded static files

