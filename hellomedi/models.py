# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class NewsRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    
    def __str__(self):
        return self.email

class News_showbiz(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/')

class Appointment(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    condition = models.CharField(max_length=300)
    preferred_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.first_name