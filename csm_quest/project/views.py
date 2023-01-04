from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Template, Context
from .models import MyModel
from django import views
from .forms import MyModelForm


# Create your views here.


def csm_view(request):
    selections = MyModelForm
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyModelForm(request.POST)
        y_n = request.POST.get("y_n")
        dmp = request.POST.get("providers")

        # check whether it's valid:
        if form.is_valid():
            if y_n == 'no' and dmp != 'none of the above':

                return HttpResponseRedirect('firstparty/')
        
            if y_n == 'yes':

                return HttpResponseRedirect('thirdparty/')
    
            if y_n == 'no' and dmp == 'none of the above':

                return HttpResponseRedirect('CRM/')
    else:
        form = MyModelForm()

    return render(request, 'csm_view.html', {'form': form})

def firstparty(request):
    return render(request,'firstparty.html')

def CRM(request):
    return render(request,'CRM.html')

def thirdparty(request):
    return render(request,'thirdparty.html')
