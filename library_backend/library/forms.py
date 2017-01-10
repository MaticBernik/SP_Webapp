from django import forms

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