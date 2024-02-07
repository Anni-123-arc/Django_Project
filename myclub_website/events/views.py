from django.shortcuts import render
from django.utils import timezone
from .models import Event,MyClubUser,Venue

from django.shortcuts import render
from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})




def home(request):
    return render(request,'home.html',{})