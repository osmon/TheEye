from typing import Tuple
from rest_framework.views import APIView
from event_processor.controller import EventProcessorController
from django.http import JsonResponse

class EventProcessorAPI(APIView):
    def post(self, request, *args, **kwargs):
        post_data = request.data
        
        if post_data['action'] =='store':
            self.store_event(post_data['event'])
        if post_data['action'] =='query':
            query_meta = post_data['query_meta']
            self.get_event(query_meta)
             
        if post_data['action'] =='date-range':
            query_meta = post_data['query_meta']
            self.get_event(query_meta)
             
    def store_event(self,event_meta):
        EventProcessorController().store_event(event_meta)
    
    def get_event(self,query_meta):
        response = EventProcessorController().event_query(query_meta)
    
        
        
        
        
    

    
   
