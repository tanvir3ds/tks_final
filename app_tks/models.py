from django.db import models

# Create your models here.

class TestClassTrial(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='test')

    def __str__(self):
        return self.title 

class Award(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='Awards')
    description = models.TextField()

    def __str__(self):
        return self.title

class Interview(models.Model):
    title = models.CharField(max_length=150)
    embed_youtube_code = models.CharField(max_length=150)
    
    
    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='Photos')

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=150)
    embed_youtube_code = models.CharField(max_length=150)
    
    
    def __str__(self):
        return self.title

class Article(models.Model):
    Subject = models.CharField(max_length=150)
    Source = models.CharField(max_length=150)
    Date = models.DateField()
    Link = models.CharField(max_length=150)

    def __str__(self):
        return self.Subject

class Press(models.Model):
    Subject = models.CharField(max_length=150)
    Source = models.CharField(max_length=150)
    Date = models.DateField()
    Link = models.CharField(max_length=150)

    def __str__(self):
        return self.Subject


class BlogCategory(models.Model):
    category= models.CharField(max_length=150)

    def __str__(self):
        return self.category
        

class Blog(models.Model):
    title = models.CharField(max_length=150)
    # slug = models.SlugField(max_length=250, null=True, blank=True)
    description = models.TextField()
    img = models.ImageField(upload_to='blog')
    category = models.ForeignKey('BlogCategory',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title