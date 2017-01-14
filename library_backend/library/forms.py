from django import forms
from .models import  Author,Book,User

class LoginForm(forms.Form):
  username = forms.CharField(label='Username:', max_length=100) #id="usernameField"
  password = forms.CharField(max_length=100, widget=forms.PasswordInput) #id="passwordField"

'''class RegisterForm(forms.Form):
  firstName = forms.CharField(label='First name:', max_length=100)
  lastName = forms.CharField(label='Last name:', max_length=100)
  address = forms.CharField(label='Address:', max_length=100)
  username = forms.CharField(label='Username:', max_length=100) #id="usernameField"
  password = forms.CharField(max_length=100, widget=forms.PasswordInput) #id="passwordField"
'''
class newBookForm(forms.Form):
  title = forms.CharField(label='Title:', max_length=100)
  author = forms.ChoiceField(label='Author', choices=[(x.firstName,x.lastName) for x in Author.objects.all()])
  genre = forms.CharField(label='Genres:', max_length=100)

class newLeaseForm(forms.Form):
  user = forms.ChoiceField(label='User', choices=[(x.first_name,x.last_name) for x in User.objects.all()])
  book = forms.ChoiceField(label='Book', choices=[(x.title) for x in Book.objects.all()])