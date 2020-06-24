from django.contrib import admin
admin.site.site_header = 'Tapan Kanti Sarkar'


# Register your models here.

from .models import TestClassTrial
admin.site.register(TestClassTrial)

from .models import Award
admin.site.register(Award)


from .models import Interview
admin.site.register(Interview)


from .models import Photo
admin.site.register(Photo)


from .models import Video
admin.site.register(Video)

from .models import Article
admin.site.register(Article)

from .models import Press
admin.site.register(Press)

from .models import BlogCategory
admin.site.register(BlogCategory)

from .models import Blog
admin.site.register(Blog)

