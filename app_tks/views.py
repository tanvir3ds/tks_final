from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

# Create your views here.
from . models import TestClassTrial
from . models import Award
from . models import Interview
from . models import Photo
from . models import Video
from . models import Article
from . models import Press
from . models import BlogCategory,Blog




def home(request):
    
    return render(request, 'home.html')


def profile(request):

    return render(request, 'profile.html')


def awards(request):
    awards = Award.objects.all()
    
    return render(request, 'awards.html',
    {'awards': awards}
    )


def blog(request):

    categorys= BlogCategory.objects.all()
    blogs=Blog.objects.all().order_by('-id') # latest
    recentblogs=Blog.objects.all().order_by('-id')[:5] 
    
    return render(request, "blog.html",
    {
        'categorys':categorys, 
        'blogs':blogs, 
        'recentblogs':recentblogs
    })


def photos(request):
    photos = Photo.objects.all()

    return render(request, 'photos.html',
    {'photos':photos}
    )

def videos(request):
    videos= Video.objects.all()

    return render(request, 'videos.html',
    {'videos': videos}
    )



def interviews(request):
    interviews = Interview.objects.all()

    
    return render(request, 'interviews.html',
    {'interviews': interviews}
    )


def article(request):
    article = Article.objects.all()
    
    return render(request, 'article.html',
    {'article': article}
    )





def press(request):
    presses = Press.objects.all()
    return render(request, 'press.html',
    {'presses': presses}
    )


def contact(request):
    
    return render(request, 'contact.html')


def test(request):
    object_tests = TestClassTrial.objects.all()
   

    return render(request, 'test.html',
    {'object_tests': object_tests}
     )





# # for unknown urls .........................
# from django.http import HttpResponse

# def error_404_view(request, exception):
    
#     return render(request,"error_404.html")


    
    
    
    