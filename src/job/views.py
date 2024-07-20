from urllib import request
from django.urls import reverse
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Job,apply
from django.core.paginator import Paginator
from .forms import ApplyForm,JobForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
# Create your views here.


def job_list(request):
    job_list=Job.objects.all()
    # filter
    myfilter=JobFilter(request.GET,queryset=job_list)
    job_list=myfilter.qs
    paginator = Paginator(job_list, 4) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    # return render(request, 'list.html', {'page_obj': page_obj})
    # context ={'jobs':job_list}
    
    context ={'jobs':page_obj,'myfilter':myfilter}
    return render(request,'job/job_list.html',context)



def job_details(request,slug):
    job_detail=Job.objects.get(slug=slug)
    
    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        print('test')
        if form.is_valid():
            
            myform = form.save(commit=False)
            myform.Job=job_detail
            myform.save()
            # form_test.created_by = request.user
            # form_test.save()
            print('done')
    else:
        form= ApplyForm()
    
    context ={'job': job_detail,'form':form}
    return render(request,'job/job_detail.html',context)

@login_required
def add_job(request):
    
    if request.method=='POST':
        form=JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            # return render(request,'job/job_list.html',)
            return redirect(reverse('jobs:job_list'))
    else:
        form=JobForm()
    
    return render(request,'job/add_job.html',{'form':form})




