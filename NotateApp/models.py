from django.db import models

# Create your models here.


class Txt (models.Model):
    TextId = models.AutoField(primary_key=True)
    Text = models.TextField()


class Tagging (models.Model):

  TagId = models.AutoField(primary_key=True)
  Start = models.IntegerField()
  Start_span_id = models.IntegerField()
  Txxt = models.TextField()
  End = models.IntegerField()
  End_span_id = models.IntegerField()
  Label = models.TextField()
  



