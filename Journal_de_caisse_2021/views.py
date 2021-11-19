from django.shortcuts import render, redirect
from django.contrib.auth import authenticate


def login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Password = request.POST['Password']

        if authenticate(request, username=Username, password=Password):
            # print(os)
            return redirect('home_page')
    return render(request,"web/login.html")