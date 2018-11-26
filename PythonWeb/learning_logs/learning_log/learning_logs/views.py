from django.shortcuts import render
from  .models import Topic

# Create your views here.

def index(request):
    return  render(request,'blog/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return  render(request,'blog/topics.html',context)