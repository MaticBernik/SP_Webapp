from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib import auth
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Book,Lease,Author

def index(request):
	if request.method=='GET':
		template=loader.get_template('login.html')
		books_list = Book.objects.all()
		context = {
			"books_list": books_list
		}
		return HttpResponse(template.render())

def books(request):
	if request.method=='GET':
		template=loader.get_template('books.html')
		books_list = Book.objects.all()
		context = {
			"books_list": books_list
		}
		return HttpResponse(template.render(context, request))

def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user=auth.authenticate(username=username,password=password)
		print(user)
		if user is not None:
			auth.login(request,user)
			return HttpResponseRedirect('books/')
		else:
			return HttpResponseRedirect('/library/') #POSLJI ZRAVEN SE SPOROCILO