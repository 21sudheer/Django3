from jan.models import Application
from jan.form import ApplicationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
# Create your views here.

def first(request):
    form=ApplicationForm()
    if request.method == 'POST':
        print("hello working")
        print(request.POST)
        form=ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponse("Data inserted")
    return render(request,'first.html',{'form':form})