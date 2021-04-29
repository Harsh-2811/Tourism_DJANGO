import datetime

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class Blog(models.Model):
    status_type = [
        ('1','Publish'),
        ('0','Draft')
    ]
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = RichTextField()
    author = models.CharField(max_length=100)
    image= models.ImageField(upload_to='blogs',default="static/images/image_1.jpg")
    status = models.CharField(choices=status_type,max_length=20)
    date = models.DateField(default=datetime.datetime.now().date())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100,default="Travel",null=True,blank=True)

    def __str__(self):
        return  self.title