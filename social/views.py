from django.shortcuts import render, redirect
from social.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.

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

@login_required
def profile(request, pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user

	args = {'user': user}
	return render(request, 'social/profile.html', args)
	
@login_required
def editprofile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect(reverse('social:profile'))

	else:
		form = EditProfileForm(instance=request.user)
		args = {'form' : form}
		return render(request, 'social/editprofile.html', args)

@login_required
def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect(reverse('social:profile'))

		else:
			return redirect(reverse('social:change-password'))


	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form' : form}
		return render(request, 'social/editpassword.html', args)


