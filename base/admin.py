from django.contrib import admin
from . models import Article_model

# Register your models here.

class Article_admin(admin.ModelAdmin):
    
    list_display=['title','desc']

admin.site.register(Article_model,Article_admin)
