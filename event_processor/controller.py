from django.shortcuts import render
from django.db.models import Q
from datetime import datetime
import datetime

class EventProcessorController:
    def store_event(self,event_meta):
        print(event_meta)