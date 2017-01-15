from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
# import the logging library
import logging
# Create your views here.
from .models import Book,Lease,Author,User,Reservation
from .forms import LoginForm,NewBookForm,NewLeaseForm

# Get an instance of a logger
logger = logging.getLogger(__name__)

def isLibrarian(user):
	if user.groups.filter(name='Librarian').exists():
		return True
	else:
		return False

def isUser(user):
	if user.groups.filter(name='User').exists():
		return True
	else:
		return False

def index(request):
	user = request.user
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
				logger.error("Unsuccessful user authentication.")
				return HttpResponseRedirect('/library/')  # POSLJI ZRAVEN SE SPOROCILO

def updateBookStatus(book_id):
	book = Book.objects.get(id=book_id)
	if not book.available:
		book_reservation = Reservation.objects.filter(book_id=book)
		book_lease = Lease.objects.filter(book_id=book)
		reserved=False
		leased=False
		if book_reservation.count() > 0:
			for reservation in book_reservation:
				if not reservation.is_expired():
					reserved=True
		if book_lease.count() > 0:
			for lease in book_lease:
				if not lease.is_expired():
					leased=True

		if reserved or leased:
			book.available=False
		else:
			book.available=True
		book.save()

@user_passes_test(isLibrarian,login_url='/library/')
def newBook(request):
	if request.method=='POST':
		book_title=request.POST['title']
		book_author=Author.objects.get(id=request.POST['author'])
		book_genre=request.POST['genre']
		book = Book(title=book_title,author=book_author,genre=book_genre)
		logger.info("Attempting to save new book(title='",book_title,"', author='",book_author,"', genre='",book_genre,"'")
		book.save()
		logger.info("Success on saving new book(title='", book_title, "', author='", book_author, "', genre='",book_genre, "'")
		#New book created successfuly
		#return HttpResponseRedirect(reverse('/library/books'))
		return HttpResponseRedirect('/library/books')
	if request.method=='GET':
		newBookForm=NewBookForm()
		template = loader.get_template('newBook.html')
		context = {
			"form": newBookForm
		}
		return HttpResponse(template.render(context))

@login_required(login_url='/library/')
def books(request):
	user = request.user
	if request.method=='GET':
		template=loader.get_template('books.html')
		books_list = Book.objects.all()
		for book in books_list:
			updateBookStatus(book.id)
		if user.groups.filter(name='Librarian').exists():
			role='Librarian'
		elif user.groups.filter(name='User').exists():
			role='User'
		else:
			logger.error("Unknown user role.")
		context = {
			"role": role,
			"books_list": books_list
		}
		return HttpResponse(template.render(context, request))

@user_passes_test(isLibrarian,login_url='/library/')
def home(request):
	if request.method=='GET':
		template=loader.get_template('home.html')
		context={}
		return HttpResponse(template.render(context, request))

@login_required(login_url='/library/')
def users(request):
	if request.method=='GET':
		template=loader.get_template('users.html')
		users_list = User.objects.all()
		context = {
			"users_list": users_list
		}
		return HttpResponse(template.render(context, request))

@login_required(login_url='/library/')
def leases(request):
	user=request.user
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

@login_required(login_url='/library/')
def reserve(request,book_id):
	user=request.user
	if request.method=='POST':
		updateBookStatus(book_id)
		book = Book.objects.get(id=book_id)
		if book.available:
			reservation = Reservation(user_id=user,book_id=book)
			reservation.save()
			book.available=False
			book.save()
			#Reservation successful
			return HttpResponseRedirect('/library/books')

@login_required(login_url='/library/')
def lease(request):
	user = request.user
	if request.method=='POST':
		book_id = request.POST['book']
		user_id = request.POST['user']
		updateBookStatus(book_id)
		book = Book.objects.get(id=book_id)
		user=User.objects.get(id=user_id)
		if book.available:
			lease = Lease(user_id=user,book_id=book)
			lease.save()
			book.available=False
			book.save()
			#Reservation successful
			return HttpResponseRedirect('/library/leases')
	if request.method == 'GET':
		template = loader.get_template('newLease.html')
		newLeaseForm = NewLeaseForm()
		context={
			'form': newLeaseForm
		}
		return HttpResponse(template.render(context))

@user_passes_test(isLibrarian,login_url='/library/')
def removeLease(request,lease_id):
	lease = Lease.objects.get(id=lease_id)
	lease.delete()
	return HttpResponseRedirect('/library/leases')

@user_passes_test(isLibrarian,login_url='/library/')
def removeBook(request,book_id):
	book = Book.objects.get(id=book_id)
	book.delete()
	return HttpResponseRedirect('/library/books')

'''def lease(request,book_id):
	if request.method=='POST':
		global user
		updateBookStatus(book_id)
		book = Book.objects.get(id=book_id)
		if book.available:
			reservation = Reservation(user_id=user,book_id=book)
			reservation.save()
			book.available=False
			book.save()
			#Reservation successful
			return HttpResponseRedirect(reverse('/library/leases'))
		if request.method == 'GET':
			template = loader.get_template('newLease.html')
			return HttpResponse(template.render())'''


'''def register(request):
	if request.method=='GET':p
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
	return HttpResponseRedirect('index')