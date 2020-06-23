from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

# Create your views here.
def home(request):
    
    return render(request, "home.html")


def profile(request):

    return render(request, "profile.html")


def awards(request):
    
    return render(request, "awards.html")


def blog(request):

    return render(request, "blog.html")


def photos(request):

    return render(request, "photos.html")

def videos(request):

    return render(request, "videos.html")



def interviews(request):
    
    return render(request, "interviews.html")


def article(request):
    
    return render(request, "article.html")


def press(request):
    
    return render(request, "press.html")


def contact(request):
    
    return render(request, "contact.html")


def test(request):
    
    return render(request, "test.html")



# # for unknown urls .........................
# from django.http import HttpResponse

# def error_404_view(request, exception):
    
#     return render(request,"error_404.html")


    
    
    
    