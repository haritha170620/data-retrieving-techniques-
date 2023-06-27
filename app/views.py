from django.shortcuts import render
from app.models import *
# Create your views here.

def display_topic(request):
    topics=Topic.objects.all()
    
    d={'topics':topics}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    #webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(id=1)
    #webpages=Webpage.objects.get(id=3)
    #webpages=Webpage.objects.exclude(id=1)
    #webpages=Webpage.objects.all().order_by('topic_name')
    #webpages=Webpage.objects.all().order_by('name')
    #webpages=Webpage.objects.all().order_by('-name')
    #webpages=Webpage.objects.all().order_by('-topic_name')
    webpages=webpage.objects.filter(date__year__='2000')

    
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    accessrecords=AccessRecord.objects.all()
    #accessrecords=AccessRecord.objects.all()
    #accessrecords=AccessRecord.objects.filter(id=3)
    #accessrecords=AccessRecord.objects.all().order_by('author')


    d={'accessrecords':accessrecords}
    return render(request,'display_accessrecord.html',d)

