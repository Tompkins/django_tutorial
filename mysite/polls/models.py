# -*- coding:utf-8 -*-
from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)     # CharField用来表示字符型字段
    pub_date = models.DateTimeField('date published') # DateField表示日期类型的字段。
    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.choice
