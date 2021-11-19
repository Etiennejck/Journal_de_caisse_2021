
#from django_auth_ldap.backend import LDAPBackend
import asyncio
import logging
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import pandas as pd

from django.urls import reverse
import uvicorn
from JournauxDeCaissePbrussels.models import *
from Journal_de_caisse_2021 import authentication_backend



def home_page(request):
    return render(request, "web/home_page.html")



def upload_file(request):
    data = {}
    if request.method == 'GET':
        return render(request,"web/upload_file.html",data)
    #if not GET
    try:
        csv_file = request.FILES["csv_file"]
        separation = request.POST['sep']
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return render(request,"web/upload_file.html")
        file_data = pd.read_csv(csv_file, sep=separation, encoding='utf-8')
        #fd = file_data[["plate_number","Charger","dateadded","Voornaam"]]
        fdi = file_data.iterrows()
        data['test']=dict(fdi)
        dfdi = dict(file_data)
        data['test2'] = dfdi
        #Payment.objects.create(**dict(fdi))
    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
        messages.error(request, "Unable to upload file. " + repr(e))

    return render(request,"web/upload_file.html",data)

@login_required
def home(request):
#     #connexion = request.POST['']

     return render(request,"web/home.html")


def log_out(request):
    response = HttpResponseRedirect(request, 'home')
    response.set_cookies('sessionid', 0)
    #
    # # response = redirect('home')
    # # response.delete_cookie()
    return response



async def client_handler(websocket,uri):
    # Send a message
    websocket.send('Hello, world')
    # Wait for a reply
    msg = websocket.recv()


async def client_handler2(websocket, uri):
    # Send a message
    websocket.send('Hello world')
    # Read all messages while the socket is open
    while True:
        msg = websocket.recv()
        if msg is None:
            # Oops, the socket has closed
            return
    # Fancy message processing
        print('got message:', msg)