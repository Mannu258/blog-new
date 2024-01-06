from django.db import models
from froala_editor.fields import FroalaField
from django.utils.text import slugify
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class blogmodel(models.Model):
    title = models.CharField(max_length = 30)
    content = HTMLField()
    slug = models.SlugField(null = True,blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blogapp')
    created_at = models.DateTimeField(auto_now_add = True)
    upload_to = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title
    # for genrate slug automaticly
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(blogmodel,self).save(*args,**kwargs)

class UserDetails(models.Model):
    Username = models.CharField(max_length = 60,blank = True, null =True)
    name = models.CharField(max_length = 30,null =True)
    email = models.EmailField(null =True)
    number = models.IntegerField(null =True)
    def __str__(self) -> str:
        return self.Username
    