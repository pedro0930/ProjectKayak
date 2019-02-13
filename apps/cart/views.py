from django.shortcuts import render, redirect
from apps.cart.models import *
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import *

def model_form_upload(request):
    if request.method == 'POST':
        print("POST request recieved")
        print('request POST content: ', request.POST)
        print('request FILES content: ', request.FILES)
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form validation success")
            form.save()
            return redirect('/')
        else:
            print("failure, attempting to print form object")
            form = DocumentForm()
            print(form)
            return redirect('/')

def index(request):
	return render(request, 'index.html')

def checkout(request):
	return render(request, 'checkout.html')