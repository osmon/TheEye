from typing import Tuple
from rest_framework.views import APIView
from event_processor.controller import EventProcessorController
from django.http import JsonResponse
from the_eye_core.settings import CLIENT_KEY

class EventProcessorAPI(APIView):
    def post(self, request, *args, **kwargs):
        post_data = request.data
        try:
            client_key = post_data['client_key']
        except:
            response={'status':401}
            return JsonResponse(response)
            
        if self.validate_client_key(client_key) is False:
            response={'status':401}
            return JsonResponse(response)

            
        
        if post_data['action'] =='store':
            return self.store_event(post_data['event'])
        
        if post_data['action'] =='query':
            query_meta = post_data['query_meta']
            return  self.get_event(query_meta)
             
        if post_data['action'] =='date-range':
            query_meta = post_data['query_meta']
            return self.get_event(query_meta)
             
    def store_event(self,event_meta):
        EventProcessorController().store_event(event_meta)
    
    def get_event(self,query_meta):
        response = EventProcessorController().event_query(query_meta)
        print(response)
        return JsonResponse({ 
                             "status":200,
                             'payload':response
                             })
        
    def validate_client_key(self,client_key):
        if CLIENT_KEY != client_key:
            return False
        else:
            return True
            
        
        
        
        
    

    
   
