from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

# Create your views here.
def parkingrights(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Password = request.POST['Password']
        if authenticate(request, username=Username, password=Password):
            return redirect('home_page')
    return render(request,"web/parkingrights.html")