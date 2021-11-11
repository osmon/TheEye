from django.db import models
    
class EventModel(models.Model):
    session_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    
    def save(self, category,payload,*args, **kwargs):
        self.category = category
        self.payload = payload
        super(EventModel, self).save(*args, **kwargs)
            
    def __unicode__(self):
        return self.id
    
class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
   
    def __unicode__(self):
        return self.id
    
class CaterogyFieldsModel(models.Model):
    field_name = models.CharField(max_length=50)
    category = models.ForeignKey(CategoryModel, on_delete = models.CASCADE,default=None)
    
    def __unicode__(self):
        return self.id

class PayloadModel(models.Model):
    event = models.ForeignKey(EventModel, on_delete = models.CASCADE,default=None)
    caterogy_field = models.ForeignKey(CaterogyFieldsModel, on_delete = models.CASCADE,null=True, blank=True)
    value = models.CharField(max_length=400,default=None,null=True, blank=True)
    
    def save(self, is_form,form_values,*args, **kwargs):
        self.is_form = is_form
        self.form_values = form_values
        super(PayloadModel, self).save(*args, **kwargs)
            
    
    def __unicode__(self):
        return self.id

class FormModel(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    payload = models.ForeignKey(PayloadModel, on_delete = models.CASCADE,default=None,null=True, blank=True)
    
    def __unicode__(self):
        return self.id

  