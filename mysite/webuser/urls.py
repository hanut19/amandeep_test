from django.urls import path, re_path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 


from . import views
#from .views import HomePageView, CreatePostView
from .views import *

urlpatterns = [
    #path('signup/', views.SignUp.as_view(), name='signup'),
    #path('', HomePageView.as_view(), name='home'),
    #path('post/', CreatePostView.as_view(), name='add_post')
    path('post/', views.upload, name='add_post'),
    path('list/', views.image_list, name='list_image'),
    re_path(r'^sub_list/(?P<id>\d+)/$', views.sub_image_list, name='sub_list_image'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)