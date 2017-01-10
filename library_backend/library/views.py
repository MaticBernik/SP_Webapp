from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Book,Lease,Author,User
from .forms import LoginForm

def index(request):
	if request.method=='GET':
		template=loader.get_template('login.html')
		books_list = Book.objects.all()
		context = {
            'loginForm': LoginForm()
		}
		return HttpResponse(template.render(context))
	elif request.method=='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'] )
			if user is not None:
				login(request, user)
				if user.groups.filter(name='Librarian').exists():
					return HttpResponseRedirect('home/')
				elif user.groups.filter(name='User').exists():
					return HttpResponseRedirect('books/')
			else:
				return HttpResponseRedirect('/library/')  # POSLJI ZRAVEN SE SPOROCILO

def books(request):
	if request.method=='GET':
		template=loader.get_template('books.html')
		books_list = Book.objects.all()
		context = {
			"books_list": books_list
		}
		return HttpResponse(template.render(context, request))

def home(request):
	if request.method=='GET':
		template=loader.get_template('home.html')
		context={}
		return HttpResponse(template.render(context, request))

def users(request):
	if request.method=='GET':
		template=loader.get_template('users.html')
		users_list = User.objects.all()
		context = {
			"users_list": users_list
		}
		return HttpResponse(template.render(context, request))

def leases(request):
	if request.method=='GET':
		template=loader.get_template('leases.html')
		leases_list = Lease.objects.all()
		context = {
			"leases_list": leases_list
		}
		return HttpResponse(template.render(context, request))

'''def register(request):
	if request.method=='GET':
		template=loader.get_template('register.html')
		return HttpResponse(template.render())
	elif request.method=='POST':
'''

'''
def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user=authenticate(username=username,password=password)
		print(user)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect('books/')
		else:
			return HttpResponseRedirect('/library/') #POSLJI ZRAVEN SE SPOROCILO
'''

def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))