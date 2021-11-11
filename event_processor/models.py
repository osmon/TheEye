from django.db import models

class FormModel(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    
    def __unicode__(self):
        return self.id
    
class PayloadModel(models.Model):
    name = models.CharField(max_length=50)
    category=models.CharField(max_length = 6)
    form = models.ForeignKey(FormModel, on_delete = models.CASCADE)
    host=models.CharField(max_length=80)
    path = models.CharField(max_length=200)
    element = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.id

class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.id

class EventModel(models.Model):
    session_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(CategoryModel, on_delete = models.CASCADE)
    timestamp = models.DateTimeField()
    
    def __unicode__(self):
        return self.id

