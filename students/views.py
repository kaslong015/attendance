from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404


# Create your views here.
def index(request):
    context = {"name":"kevin"}
    return render(request,'index.html',context)