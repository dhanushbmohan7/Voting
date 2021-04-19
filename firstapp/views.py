from django.shortcuts import render,redirect
import time
from .models import Poll
def index(request):
    data=Poll.objects.all()
    return render(request,'index.html',{'data':data})

def voting(request):
    
    if request.method=='GET':
        name =request.GET.get('name')
        print(name)
    else:
        print('no name')    
    
    candidate=Poll.objects.get(candidate_name=name)
    vote_count=candidate.vote_count
    vote_count+=1
    candidate.vote_count=vote_count
    candidate.save()
    print(vote_count)
    
    data=Poll.objects.all()
    
    return render(request,'index.html',{'data':data,'img':candidate.candidate_logo})
    print('function enmded')
    

