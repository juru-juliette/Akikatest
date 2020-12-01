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