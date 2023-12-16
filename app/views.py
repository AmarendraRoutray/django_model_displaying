from django.shortcuts import render

# Create your views here.
from app.models import *

#------TOPIC
def display_topics(request):
    QLTO=Topic.objects.all()
    d = {'topics':QLTO}
    return render(request,'display_topics.html',d)

# inserting data into topic 
def insert_topic(request):
    tn = input('Enter topic name: ')
    TNO = Topic.objects.get_or_create(topic_name=tn)[0]
    TNO.save()
    
    QLTO=Topic.objects.all()
    d = {'topics':QLTO}
    return render(request,'display_topics.html',d)



#-------WEBPAGE
def display_webpage(request):
    QLWO = Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


# inserting data into webpage
def insert_webpage(request):
    tn=input('Enter topic name: ')
    n=input('Enter name: ')
    u=input('Enter url: ')
    e=input('Enter email: ')
    TO=Topic.objects.get(topic_name=tn)
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()
    
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)



#--------AccessRecord
def display_accessrecord(request):
    QLARO=AccessRecord.objects.all()
    d={'accessrecord':QLARO}
    return render(request,'display_accessrecord.html',d)

def insert_accessrecord(request):
    n=input('Enter name: ')
    a=input('Enter author: ')
    d=input('Enter date: ')
    WO=Webpage.objects.get(name=n)
    ARO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    ARO.save()
    
    QLARO=AccessRecord.objects.all()
    d={'accessrecord':QLARO}
    return render(request,'display_accessrecord.html',d)
    
    