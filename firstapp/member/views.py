from django.template import loader
from django.http import HttpResponse
from member.models import Member
from django.shortcuts import render

def member(request):
    mymembers = Member.objects.all().values()
    template=loader.get_template('myfirst.html')
    context = {
        'mymembers': mymembers,
    }
    # return HttpResponse(template.render(context, request))
    return render(request,'myfirst.html',context)

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember':mymember,
    }
    return  HttpResponse(template.render(context, request))

