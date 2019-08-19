from django.contrib import admin

from django.contrib import admin
from . models import *

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Catagory)
admin.site.register(Problem)

