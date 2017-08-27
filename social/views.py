from django.shortcuts import render, redirect
from social.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def home(request):
	return render(request, 'social/home.html')


def register(request):
	if request.method =='POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, 'social/registration.html', args)


def profile(request):
	args = {'user' : request.user}
	return render(request, 'social/profile.html', args)

def editprofile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/profile')

	else:
		form = EditProfileForm(instance=request.user)
		args = {'form' : form}
		return render(request, 'social/editprofile.html', args)


def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/profile')

		else:
			return redirect('/edit-password')


	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form' : form}
		return render(request, 'social/editpassword.html', args)


