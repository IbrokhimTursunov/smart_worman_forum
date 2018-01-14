from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Forum_account

def logon_func(request):
    return render(request, 'logon_page.html')

def new_user_func(request):
    return render(request, 'new_account_page.html')

def new_user_create_func(request):
    logon_data = {'username' : request.POST['account_username'],
                  'first_name' : request.POST['account_name'],
                  'last_name' : request.POST['account_lastname'],
                  'password0' : request.POST['account_password_0'],
                  'password1' : request.POST['account_password_1']
                 }
    #Forum_account.objects.create(
    return render(request, 'test_page.html')
