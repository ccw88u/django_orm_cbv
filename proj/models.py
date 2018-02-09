# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


# Create your models here.
class Reguser(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    addr = models.CharField(max_length=254)
    tel = models.CharField(max_length=128)      
    email = models.EmailField(max_length=190, unique=True)
    # pip install pillow to use this!
    # Optional: pip install pillow 
    # upload_to='profile_pics' => save to media/profile_pics dir
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


class website_subject(models.Model):
    subject_name = models.CharField(max_length=190, unique=True)

    def __unicode__(self): 
    # 在Python3中使用 def __str__(self):        
        return u"%s" % (self.subject_name)

class website(models.Model):
    title = models.CharField(max_length=200)
    ## as flybase tableitem
    subject = models.ForeignKey(website_subject) 
    uri = models.URLField(blank=True) 
    date = models.DateField()

    def __unicode__(self): 
    # 在Python3中使用 def __str__(self):        
        return u"%s" % (self.title)



########################公司資訊 簡目 / 列出成員 / 新增 / 刪除 / 修改{S}########################
## 公司資訊
class company(models.Model):
    name = models.CharField(max_length=256)
    tel  = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    
    def __unicode__(self): 
        return u"%s" % (self.name)

    def get_absolute_url(self):
        return reverse("detail", kwargs={'pk':self.pk})

## 公司成員
class member(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    member = models.ForeignKey(company, related_name='members')

    def __unicode__(self): 
        return u"%s" % (self.name)

########################公司資訊 簡目 / 列出成員 / 新增 / 刪除 / 修改{E}########################