import logging

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
import pandas as pd
from django.urls import reverse

from JournauxDeCaissePbrussels.models import *


def home_page(request):
    return render(request, "web/home_page.html")

def upload_file(request):
    data = {}
    if request.method == 'GET':
        return render(request,"web/upload_file.html",data)
    #if not GET
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return render(request,"web/upload_file.html")
        file_data = pd.read_csv(csv_file, sep=';')
        fd = file_data[["plate_number","Charger","dateadded","Voornaam","creator_lastname"]]
        fdi = fd.iterrows()
        data['test']=dict(fdi)
        dfdi = dict(fd)
        data['test2'] = dfdi
        #Payment.objects.create(**dict(fdi))
    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
        messages.error(request, "Unable to upload file. " + repr(e))

    return render(request,"web/upload_file.html",data)