from django import forms
from .models import  Author,Book,User
from django.contrib.auth.forms import UserCreationForm

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
class NewBookForm(forms.Form):
  title = forms.CharField(label='Title:', max_length=100)
  #author = forms.ChoiceField(label='Author', choices=[x.firstName+" "+x.lastName for x in Author.objects.all()])
  author = forms.ModelChoiceField(label='Author', queryset=Author.objects.all())
  genre = forms.CharField(label='Genres:', max_length=100)

class NewLeaseForm(forms.Form):
  user = forms.ModelChoiceField(label='user', queryset=User.objects.all())
  book = forms.ModelChoiceField(label='book', queryset=Book.objects.filter(available=True))

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields=['first_name','last_name','email','username','password']
    widgets = {
      'password': forms.PasswordInput(),
      'email': forms.EmailInput(attrs={'placeholder': 'something@something.com'}),
    }

class UserCreateForm(UserCreationForm):
  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")

  def save(self, commit=True):
    user = super(UserCreateForm, self).save(commit=False)
    user.email = self.cleaned_data["email"]
    if commit:
      user.save()
    return user