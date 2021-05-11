from django import forms

class RegisterForm(forms.Form):
	user_first_name = forms.CharField(max_length = 100)
	user_last_name = forms.CharField(max_length = 100)
	user_email = forms.CharField()
	user_password = forms.EmailField()

