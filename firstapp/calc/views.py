from django.http import HttpResponse
from calc.models import Employee
from calc.forms import EmployeeForm
from django.shortcuts import render,redirect
from django.template import loader


# Create your views here.
def index(request):

   template=loader.get_template('index.html')
   #context={'mynumber': 8947397598,}
   #context={'fruits':['Apple','Banana','Cherry']}
   return HttpResponse(template.render()) 
   #context={'size':2621400}
   #context={'var1':'John\nDoe',}
   
    
   #context={'prices':[56,55,32],}
   #context = {'name':"Capt'n Jack",}
   #context={'animal':"tiger",}
   #context={'name':'sudheer',}
   #context={'colors':['red','green','blue','','yellow']}
#    context={
#        'cars':[
#             {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
#             {'brand': 'Volvo', 'model': 'XC90', 'year': 2022},
#        ]
#    }
     
 
#     form = EmployeeForm()
#     if request.method == 'POST':
#         print("hello working")
#         print(type(request.POST))
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()

#             return HttpResponse("data inserted")
#     return render(request, 'index.html', {'form':form})

def details(request):
    data=Employee.objects.all()
    return render(request,'details.html', {'data':data})

def update(request, i):
    employee = Employee.objects.get(id=i)
    form=EmployeeForm(instance=employee)
    if request.method == "POST":
        form=EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        return redirect('details')
    return render(request,'update.html',{'form': employee})

def delete(request,id):
    form=Employee.objects.get(id=id)
    form.delete()
    return redirect('details')

def home(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass

    else:
        form=EmployeeForm()
    return render(request,'index.html',{'form':form})


def testing(request):
    template=loader.get_template('template.html')
    context={
        'heading':'Hello &lt;i&gt;my&lt;/i&gt; World',
    }
    return HttpResponse(template.render(context, request))

def block(request):
    template=loader.get_template('child_temp.html')
    return HttpResponse(template.render())

def comment(request):
    template=loader.get_template('comment.html')
    return HttpResponse(template.render())

def cycle(request):
    template=loader.get_template('cycle.html')
    context={
        'fruits':['Apple','Banana','Cherry','Orange']
    }
    return HttpResponse(template.render(context,request))