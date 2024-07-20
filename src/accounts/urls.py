from django.urls import path
from accounts.views import signup,profile,profile_edit
app_name='job'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('profile/',profile,name='profile'),
    path('profile/edit/',profile_edit,name='profile_edit'),
    
]