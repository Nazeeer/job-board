from django.urls import path
from home.views import show
app_name='job'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',show,name='show'),
    
]