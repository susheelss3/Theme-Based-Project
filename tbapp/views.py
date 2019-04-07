from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    md={'insert_me':'Em ledhu sheyy'}
    return render(req,'tbapp/index.html',context=md)

def login(req):
    return render(req,'tbapp/login.html')