from django.shortcuts import render
from event_processor.models import FormModel,PayloadModel,CategoryModel,EventModel,CaterogyFieldsModel
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
import datetime

class EventProcessorController:
    def store_event(self,event_meta):
        print(event_meta)
        event=EventModel(
                    session_id = event_meta['session_id'],
                    name = event_meta['name'],
                    timestamp = event_meta['timestamp']
            )
        payload = event_meta['data']
        category_name = event_meta['category']
        event.save(category_name,payload)
    
    def event_query(self,query_meta):
        if query_meta['filter'] == 'session':
            return self.__get_events_by_session(query_meta)    
          
        if query_meta['filter'] == 'category':
            return self.__get_events_by_category(query_meta)
                  
        if query_meta['filter'] == 'date-range':
            return self.__get_events_by_date_range(query_meta)
                
    def __get_events_by_session(self,query_meta):
            session_events={}
            event_query = EventModel.objects.filter(session_id=query_meta['value'])
            for event_meta in event_query:
                session_events['%s'%event_meta.session_id]=[]
            for event_meta in event_query:
                payload_query = PayloadModel.objects.filter(event_id = event_meta.id)
                for payload in payload_query:
                    meta_value = payload.value
                    if payload.caterogy_field.category.name == "form interaction":
                        form_values_query = FormModel.objects.get(payload_id=payload.id)
                        form_values={
                            "first_name":form_values_query.first_name,
                            "last_name":form_values_query.last_name
                        }
                    else:
                        form_values=None
                        
                    session_events[event_meta.session_id].append({
                        'timestamp':event_meta.timestamp,
                        'name':event_meta.name,
                        'category':payload.caterogy_field.category.name,
                        'meta':payload.caterogy_field.field_name,
                        'meta_value':meta_value,
                        'form_values':form_values
                    })
            return session_events
                    
    def __get_events_by_category(self,query_meta): 
            category_events={}
            payload_query = PayloadModel.objects.filter(caterogy_field__category__name=query_meta['value'])
            for payload_meta in payload_query:
                category_events['%s'%payload_meta.caterogy_field.category.name]=[]
            
            for payload_meta in payload_query:
                meta_value = payload_meta.value
                if payload_meta.caterogy_field.field_name == "form":
                        form_values_query = FormModel.objects.get(payload_id=payload_meta.id)
                        form_values={
                            "first_name":form_values_query.first_name,
                            "last_name":form_values_query.last_name
                        }
                else:
                    form_values=None
                category_events[payload_meta.caterogy_field.category.name].append({
                    'session_id':payload_meta.event.session_id,
                    'timestamp':payload_meta.event.timestamp,
                    'event_name':payload_meta.event.name,
                    'meta':payload_meta.caterogy_field.field_name,
                    'meta_value':meta_value,
                    'form_value':form_values,
                })
            return category_events
    
    def __get_events_by_date_range(self,query_meta): 
            date_range_events=[]
            init_date=None
            end_date=None
            event_query = EventModel.objects.filter(timestamp__gte = init_date,timestamp__lte=end_date)
            for event_meta in event_query:
                payload_query = PayloadModel.objects.filter(event_id = event_meta.id)
                for payload in payload_query:
                    meta_value = payload.value
                    if payload.caterogy_field.category.name == "form interaction":
                        form_values_query = FormModel.objects.get(payload_id=payload.id)
                        form_values={
                            "first_name":form_values_query.first_name,
                            "last_name":form_values_query.last_name
                        }
                    else:
                        form_values=None
                        
                    date_range_events[event_meta.session_id].append({
                        'timestamp':event_meta.timestamp,
                        'name':event_meta.name,
                        'category':payload.caterogy_field.category.name,
                        'meta':payload.caterogy_field.field_name,
                        'meta_value':meta_value,
                        'form_values':form_values
                    }) 
            return date_range_events
                     
    @receiver(post_save, sender=EventModel)
    def store_event_meta(sender, instance, **kwargs):
        category_id = CategoryModel.objects.get(name=instance.category).id
        category_fields = CaterogyFieldsModel.objects.filter(category_id = category_id)
    
        for field in category_fields:
            is_form=False
            form_values=None
            payload = PayloadModel(
                event_id = None,
                caterogy_field_id = None,
                value = None,
            )
            try:
                if field.field_name != 'form':
                    value = instance.payload[field.field_name]
                    payload.event_id = instance.id
                    payload.caterogy_field_id =  field.id
                    payload.value = value
                   
            
                if field.field_name == 'form':
                    form_values = instance.payload[field.field_name]
                    is_form = True
                    payload.event_id = instance.id
                    payload.caterogy_field_id =  field.id
                    payload.value = None
            except:
                continue
            
            payload.save(is_form,form_values)
    
    @receiver(post_save, sender=PayloadModel)
    def save_form(sender, instance, **kwargs):
        if instance.is_form is True:
            form=FormModel(
                
                first_name=instance.form_values['first_name'],
                last_name=instance.form_values['last_name'],
                payload_id=instance.id
            )
            form.save()
        
    

        
        
