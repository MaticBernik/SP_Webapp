from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Book,Lease,Author,User,Reservation
from .forms import LoginForm
user=None

def index(request):
	global user
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

def updateBookStatus(book_id):
	book = Book.objects.get(id=book_id)
	if not book.available:
		book_reservation = Reservation(book_id=book_id).objects
		book_lease=Lease(book_id=book_id).objects
		if book_lease and book_lease.is_expired():
			book.available=True
		if book_reservation and book_reservation.is_expired():
			book.available = True
			#delete expired reservation
		book.save()

def books(request):
	global user
	if request.method=='GET':
		template=loader.get_template('books.html')
		books_list = Book.objects.all()
		if user.groups.filter(name='Librarian').exists():
			role='Librarian'
		elif user.groups.filter(name='User').exists():
			role='User'
		context = {
			"role": role,
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
		if user.groups.filter(name='Librarian').exists():
			leases_list = Lease.objects.all()
			role = 'Librarian'
		elif user.groups.filter(name='User').exists():
			leases_list=Lease.objects.filter(user_id=user)
			role= 'User'
		context = {
			"role": role,
			"leases_list": leases_list
		}
		return HttpResponse(template.render(context, request))

def reserve(request,book_id):
	global user
	updateBookStatus(book_id)
	book = Book.objects.get(id=book_id)
	if book.available:
		reservation = Reservation(user_id=user,book_id=book)
		reservation.save()
		book.available=False
		book.save()
		#Reservation successful
		return HttpResponseRedirect(reverse('/library/books'))


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