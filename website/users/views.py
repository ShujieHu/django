# users/views.py

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
import requests
import time
from rest_framework import status
from rest_framework.response import Response
import subprocess
import os
from .forms import CountryForm


def dashboard(request):
    return render(request, "dashboard.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))


def run_model(request):
    # this should be POST request
    if request.method == 'POST':
        form = CountryForm(request.POST)
        # first check if it is valid
        if form.is_valid():
            # process the form
            country = form['country'].value()
            print('country is', country)
            firstArg = "NB_ARGS=" + country
            bashCmd = ['/Users/shujie/Documents/CPT_HU/Semester5/CISC695/project/app4/venv/bin/jupyter', 'nbconvert', '--to', 'html',
                       'da/analysis_world.ipynb', '--execute']

            process = subprocess.Popen(
                bashCmd, stdout=subprocess.PIPE, env={'NB_ARGS': country})
            output, err = process.communicate()
            # print('Output is', output)
            # process = subprocess.Popen(['pwd'], stdout=subprocess. PIPE)
            # output, err = process.communicate()
            # print('##### Output2 is #####', output)
            if err is not None:
                print('Error is', err)
            # lookup the folder da for analysis_world.html file, if it exists render it

            print("Done processing")
            # When the operation is done, redirect to other page
            return redirect('/redirect_report')
            # return redirect('http://google.com')

        else:
            print("form is not valid")

    else:
        form = CountryForm()
    return render(request, 'run_model.html', {'form': form})
    # return render(request, 'analysis_world.html')


def redirect_report(request):
    # return render('http://www.google.com')
    return render(request, 'analysis_world.html')
