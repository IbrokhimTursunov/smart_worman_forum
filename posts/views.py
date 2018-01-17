from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Forum_account
from django.contrib.auth import authenticate, login

def login_func(request):
    return render(request, 'logon_page.html', {'error_message': ''})

def login_func_success(request):
    logon_data = {'username' : request.POST['account_username'],
                  'password' : request.POST['account_password']
                 }
    current_user = authenticate(request, username = logon_data['username'], password = logon_data['password'])
    if current_user is not None:
        login(request, current_user)
        return render(request, 'test_page.html')
    else:
        return redirect('/login', {'error_message': 'Что-то пошло не так. Проверьте ваши данные еще раз.'})


def new_user_func(request):
    return render(request, 'new_account_page.html')

def new_user_create_func(request):
    logon_data = {'username' : request.POST['account_username'],
                  'first_name' : request.POST['account_name'],
                  'last_name' : request.POST['account_lastname'],
                  'password0' : request.POST['account_password_0'],
                  'password1' : request.POST['account_password_1']
                 }
    Forum_account.objects.create_user(username = logon_data['username'],
                                 first_name = logon_data['first_name'],
                                 last_name = logon_data['last_name'],
                                 password = logon_data['password0']
                                )
    return render(request, 'test_page.html')
