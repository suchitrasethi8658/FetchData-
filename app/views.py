from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length
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
    a=AccessRecords.objects.get_or_create(name=w,date='1999-01-04')[0]
    a.save()
    return HttpResponse('Successfully Created')

def topics(request):
    LOT=Topics.objects.all() #all in the form of insertion order
    LOT=Topics.objects.order_by('topic_name') #all in the form of ascending order
    LOT=Topics.objects.order_by('-topic_name') #all in the form of ascending order
    d={'topic_name':LOT}
    return render(request,'topics.html',d)
def webpages(request):
    LOW=Webpages.objects.all()#all in the form of insertion order
    LOW=Webpages.objects.order_by(Length('topic_name').desc())#all in the form of descending order by length
    LOW=Webpages.objects.order_by(Length('topic_name'))#all in the form of ascending order by length
    LOW=Webpages.objects.exclude(topic_name='Physics')#exclude Physics
    d={'webpage_name':LOW}
    return render(request,'webpages.html',d)
def access_records(request):
    LOA=AccessRecords.objects.all()#all in the form of insertion order
    LOA=AccessRecords.objects.filter(date__gt='2022-07-07')#greater than '2022-07-07'
    LOA=AccessRecords.objects.filter(date__lte='2022-07-07')#less than equal '2022-07-07'
    LOA=AccessRecords.objects.filter(date__gte='2000-07-07')#greater than equal'2000-07-07'
    LOA=AccessRecords.objects.filter(date__lt='2021-07-07')#less than equal '2021-07-07'
    LOA=AccessRecords.objects.filter(date__year__gt='2000')#search by year only
    LOA=AccessRecords.objects.filter(date__day='07')#search by day only
    LOA=AccessRecords.objects.filter(date__month__gte='04')#search by month only
    d={'records':LOA}
    return render(request,'access_records.html',d)

