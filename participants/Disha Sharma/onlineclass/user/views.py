from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #inbuilt django method to create form instead of creating by js
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request,'user/register.html',{'form':form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')




