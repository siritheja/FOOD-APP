from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
# Create your views here.


#def register(request):
#    print("request",request.method)
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#        print("inside register")
#        if form.is_valid():
#            username = form.cleaned_data.get('username')            
#            messages.success(request,f'Welcome {username} , your account is created')
#            form.save()
#            return redirect('food:index')
#    else:
#        print("inside forms")
#        form = UserCreationForm()
#    return render(request,'users/register.html',{'form':form})

def register(request):
    print("request",request.method)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print("inside register")
        if form.is_valid():
            username = form.cleaned_data.get('username')            
            messages.success(request,f'Welcome {username} , your account is created')
            form.save()
            return redirect('login')
    else:
        print("inside forms")
        form = RegistrationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')