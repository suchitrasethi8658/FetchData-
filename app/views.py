from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def createTopics(request):
    t=Topics.objects.get_or_create(topic_name='Math')[0]
    t.save()
    return HttpResponse('Successfully Created')
def createWebpages(request):
    t=Topics.objects.get_or_create(topic_name='Math')[0]
    t.save()
    w=Webpages.objects.get_or_create(topic_name=t,name='suchitra',url='https://suchitra.com')[0]
    w.save()
    return HttpResponse('Successfully Created')
def createRecords(request):
    t=Topics.objects.get_or_create(topic_name='Computer')[0]
    t.save()
    w=Webpages.objects.get_or_create(topic_name=t,name='sanghamitra',url='https://sanghamitra.com')[0]
    w.save()
    a=AccessRecords.objects.get_or_create(name=w,date='2022-08-07')[0]
    a.save()
    return HttpResponse('Successfully Created')

def topics(request):
    LOT=Topics.objects.all()
    d={'topic_name':LOT}
    return render(request,'topics.html',d)
def webpages(request):
    LOW=Webpages.objects.all()
    d={'webpage_name':LOW}
    return render(request,'webpages.html',d)
def access_records(request):
    LOA=AccessRecords.objects.all()
    d={'records':LOA}
    return render(request,'access_records.html',d)

