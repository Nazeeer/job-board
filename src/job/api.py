from pyexpat import model
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from rest_framework import generics

from job import serializers
@api_view(['GET'])
def job_list_api(request):
    all_jobs=Job.objects.all()
    data=JobSerializer(all_jobs,many=True).data
    return Response({'data':data})


@api_view(['GET'])
def job_detail_api(request,id):
    job_detail= Job.objects.get(id=id)
    data=JobSerializer(job_detail).data
    return Response({'data':data})



class JobListApi(generics.ListCreateAPIView):
    # model=Job
    queryset=Job.objects.all()
    serializer_class=JobSerializer 


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer 
    lookup_field='id'
    