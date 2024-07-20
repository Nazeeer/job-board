# from django.contrib import admin
from django.urls import path
from job.views import job_details,job_list,add_job
from . import views
from . import api
from .api import job_list_api,job_detail_api,JobListApi,JobDetail
app_name='job'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',job_list,name='job_list'),
    path('add/',add_job,name='add_job'),
    path('<str:slug>',job_details,name='job_detail'),
    
    # api
    path('api/list/',job_list_api,name='job_list_api'),
    path('api/jobs/<int:id>',job_detail_api,name='job_detail_api'),
    
    # class  passed views
    path('api/v2/jobs/',JobListApi.as_view(),name='JobListApi'),
    path('api/v2/jobs/<int:id>',JobDetail.as_view(),name='JobDetail'),
    
]