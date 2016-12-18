from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.

def index(request):
	if request.method=='GET':
		index=loader.get_template('index.html')
		return HttpResponse(template.render())
