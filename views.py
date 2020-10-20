from django.shortcuts import render, redirect
from .forms import CreateUserForm
from .models import Contact, Small_contact
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.

def hi(request):
    return render(request, 'pages/hi.html')

def portfolio(request):
    return render(request, 'pages/portfolio.html')

def accountPage(request):
    return render(request,'pages/account.html')

def UserEditView(request):
    form_class = UserChangeForm
    #template_name = 'pages/edit_profile.html'
    success_url = reverse_lazy('home')
    return render(request, 'pages/edit_profile.html')




def contact(request):
    if request.method =='POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r,subject=subject_r,message=message_r)
        c.save()

        return render(request, 'pages/thank.html')
    else:
        return render(request, 'pages/contact.html')

# def small_c(request):
#     if request.method =='POST':
#         email_s = request.POST.get('email')
#         message_s = request.POST.get('message')
#
#         c = Small_contact(email=email_s, message=message_s)
#         c.save()
#
#         return render(request, 'personal_portfolio/base.html')
#     else:
#         return render(request, 'personal_portfolio/base.html')

def loginpage(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorect')


    context = {}
    return render(request, 'pages/login.html', context)

def registerPage(request):
    form = CreateUserForm()


    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'pages/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

