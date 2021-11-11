from typing import Tuple
from rest_framework.views import APIView
from event_processor.controller import EventProcessorController
from django.http import JsonResponse

class EventProcessorAPI(APIView):
    def post(self, request, *args, **kwargs):
        post_data = request.data
        
        if post_data['action'] =='store':
            self.store_event(post_data['event'])    
            
    def store_event(self,event_meta):
        EventProcessorController().store_event(event_meta)
    
   
