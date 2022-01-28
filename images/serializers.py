from rest_framework import serializers
from images.models import Image, Comment

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, required=False) #Optional nested serializer for returning the image with corresponding comments, if needed.
    class Meta:
        model = Image
        fields = '__all__'

