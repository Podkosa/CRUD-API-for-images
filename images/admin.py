from django.contrib import admin
from images.models import Comment, Image

class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 1
    readonly_fields = ['img', 'date_post', 'date_updated']
    
class ImagesAdmin(admin.ModelAdmin):
    inlines = [CommentsInline]
    readonly_fields = ['date_upload', 'date_updated']

admin.site.register(Image, ImagesAdmin)
