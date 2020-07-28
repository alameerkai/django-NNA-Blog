from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_filter = ['active','created']
    list_display = ['title','created' ,'active' ]
    search_fields = ['title' , 'content']

admin.site.register(Post , PostAdmin)

# Register your models here.
