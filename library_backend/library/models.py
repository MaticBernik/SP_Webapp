from django.db import models
from datetime import datetime,timedelta
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
#from django.contrib.auth.models import User_Group


# Create your models here.
#also use:
#auth_group (id,name)
#auth_user (id,password,last_login,is_superuser,first_name,last_name,email,is_staff,is_active,date_joined,username)
#auth_user_groups (id,user_id,group_id)
	
class Author(models.Model):
	#author_id --> ze po defaultu
	firstName=models.CharField(max_length=100, null=False)
	lastName=models.CharField(max_length=100, null=False)

	def __str__(self):
		return self.firstName+' '+self.lastName

class Book(models.Model):
	#book_id --> ze po defaultu
	title = models.CharField(max_length=100, null=False)
	added_date = models.DateTimeField(default=datetime.now())
	author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
	genre = models.CharField(max_length=10,null=True)
	available = models.BooleanField(default=True)

	def __str__(self):
		return self.author.firstName+' '+self.author.lastName+': '+self.title

class Lease(models.Model):
	#lease_id  --> ze po defaultu
	user_id= models.ForeignKey(User,on_delete=models.CASCADE) 
	book_id= models.ForeignKey(Book,on_delete=models.CASCADE)
	start_date= models.DateTimeField(default=datetime.now())
	expiration_date = models.DateTimeField(default=datetime.now() + timedelta(days=14))

	def __str__(self):
		return str(self.start_date)+': '+self.user_id.first_name+' '+self.user_id.last_name+' - '+self.book_id.title