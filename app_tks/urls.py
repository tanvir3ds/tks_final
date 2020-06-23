from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name= 'home'),
    path('profile', views.profile, name= 'profile'),
    path('awards', views.awards, name= 'awards'),
    path('photos', views.photos, name= 'photos'),
    path('blog', views.blog, name= 'blog'),
    path('interviews', views.interviews, name= 'interviews'),
    path('article', views.article, name= 'article'),
    path('press', views.press, name= 'press'),
    path('contact', views.contact, name= 'contact'),
    path('test', views.test, name= 'test'),
    path('videos', views.videos, name= 'videos'),
 

 
]
