from django.shortcuts import render, HttpResponse, render_to_response


# Create your views here.

def index(request):
    return render_to_response('temp.html',{'name':"VALUE"} )

def category(request, id):
    return HttpResponse('CATEGORY')