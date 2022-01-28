from rest_framework import viewsets
from .models import Image, Comment
from .serializers import ImagesSerializer, CommentsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.renderers import TemplateHTMLRenderer

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'images.html'
    
    #Uniqueness of images - 'name' field of the Image model. This can be easily changed to the name of the uploaded file, if needed.
    #Uniqueness of comments - 'text' field.
    @action(detail=False, methods=['get'])
    def stat(self, *args, **kwargs):
        queryset_images = Image.objects.all()
        queryset_comments = Comment.objects.all()

        return Response(data={
            'total_images':queryset_images.count(), 
            'unique_images':queryset_images.values('name').distinct().count(), 
            'size_images_MB':queryset_images.aggregate(size_images=Sum('size'))['size_images']/1e+6,
            'total_comments':queryset_comments.count(),
            'unique_comments':queryset_comments.values('text').distinct().count()
            }, template_name = 'stat.html')

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'comments.html'
