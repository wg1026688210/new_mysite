from django.db import models
from django.utils import timezone
import datetime
import time
from django.db import connection

# Create your models here.
class DefineManager(models.Manager):
    def findquestionall(self):
        cursor =connection.cursor()
        cursor.execute(""" select * from polls_question""")
#         return  cursor.fetchall()
        return [[row[0],row[1],row[2]] for row in cursor.fetchall()]
    def finddicall(self):
        cursor =connection.cursor()
        cursor.execute(""" select * from polls_question""")
        desc =cursor.description
#         return desc
        return [
                dict(zip([col[0] for col in desc],row)) for row in cursor.fetchall()
                 ]       
class Question(models.Model):
    def __unicode__(self):
        return self.question_test
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
    question_test =models.CharField(max_length=200)
    pub_date =models.DateTimeField(default=datetime.datetime.now)
    objects =models.Manager()
    custom = DefineManager()
    
    

class Choice(models.Model):
    question =models.ForeignKey(Question)
    choice_text =models.CharField(max_length=200)
    votes =models.IntegerField(default=0)
    def __unicode__(self): 
        return self.choice_text


            