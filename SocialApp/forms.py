from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model
)
from .models import News

User = get_user_model()


class UserLoginForm(forms.Form):
	username	= forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Username'}))
	password	= forms.CharField(label='', widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Password'}))

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This user does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")
			if not user.is_active:
				raise forms.ValidationError("This user is not active")
		return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Username'}))
	first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'First name'}))
	last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Last name'}))
	email = forms.CharField(label='', widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : 'Email'}))
	password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Confirm password'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Password'}))

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password',
			'password2'
			]

	def clean(self, *args, **kwargs):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password != password2:
			raise forms.ValidationError("Passwords must match")
		return super(UserRegisterForm, self).clean(*args, **kwargs)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		username_qs = User.objects.filter(username=username)
		if username_qs.exists():
			raise forms.ValidationError("This username is already being used")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email is already being used")
		return email


class NewsPostForm(forms.ModelForm):
	user = forms.IntegerField(required = False)
	subject = forms.CharField(
		label='', 
		widget=forms.TextInput(attrs={
			'style'			: 'width: 1340px;', 
			'placeholder'	: 'Input your subject',
			'autocomplete'	: 'off',
			'required'		: 'true'}))
	text = forms.CharField(
		label='', 
		widget=forms.Textarea(attrs={
			'style'			: 'width: 1340px; height: 250px;', 
			'placeholder'	: 'Input your news',
			'autocomplete'	: 'off',
			'required'		: 'true',
			'spellcheck'	: 'true'}))
	
	class Meta:
		model = News
		fields = [
			'user',
			'subject',
			'text'
			]

	def clean(self, *args, **kwargs):
		subject = self.cleaned_data.get('subject')
		text = self.cleaned_data.get('text')
		if not subject:
			raise forms.ValidationError("Subject field couldn`t be empty")
		if not text:
			raise forms.ValidationError("Text field couldn`t be empty")
		return super(NewsPostForm, self).clean(*args, **kwargs)

	def clean_subject(self):
		subject = self.cleaned_data.get('subject')
		if not subject:
			raise forms.ValidationError("Subject field couldn`t be empty")
		return subject

	def clean_text(self):
		text = self.cleaned_data.get('text')
		if not text:
			raise forms.ValidationError("Text field couldn`t be empty")
		return text


