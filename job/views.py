from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator


# Create your views here.


def job_list(request) :
    job_list = Job.objects.all()

    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj =paginator.get_page(page_number)

    context = {'Jobs' : page_obj}
    return render(request, 'job/job_list.html', context)

def job_detail (request, slug) : 
    job_detail = Job.objects.get(slug =slug)
    context = {'Job' : job_detail}
    return render(request, 'job/job_detail.html', context)
