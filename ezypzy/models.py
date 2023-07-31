from django.db import models
from core import secrets
from storages.backends.s3boto3 import S3Boto3Storage

AWS_STORAGE_BUCKET_NAME = secrets.AWS_STORAGE_BUCKET_NAME

AWS_ACCESS_KEY_ID = secrets.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = secrets.AWS_SECRET_ACCESS_KEY
AWS_S3_REGION_NAME = secrets.AWS_S3_REGION_NAME
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False

class S3MediaStorage(S3Boto3Storage):
    location = 'media'
# Create your models here.
class fileTable(models.Model):
    fileId= models.AutoField(primary_key=True, blank=False)
    fileType= models.CharField(max_length=100, blank=False)
    fileName= models.CharField(max_length=100, blank=False)
    file= models.FileField(storage=S3MediaStorage(),upload_to='documents/')
    deviceId= models.CharField(max_length=250, blank=False)
    converted= models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

