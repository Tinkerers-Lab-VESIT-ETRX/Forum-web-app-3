
from django.contrib import admin
from django.urls import path
from django.contrib import admin

from django.urls import include, path

from blog import views

urlpatterns = [

   path('', views.blog_list),

   path('posts/', include('blog.urls')),

   path('admin/', admin.site.urls),

]
