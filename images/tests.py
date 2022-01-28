from django.urls import reverse
from rest_framework.test import APITestCase
from ImagiON_test.settings import MEDIA_ROOT
from .models import Comment, Image
from .serializers import CommentsSerializer
import os

class ImagesViewSetTestCase(APITestCase):

    #Testing with user-uploaded images got a bit tricky, because during the testing they are uploaded to testerver, which results in 'img' path
    #being different and not comparing properly with the output of a serializer. And since there is date-time assignment - standard response cannot be hardcoded.
    #I have not been able to find a quick workaround in given time, so this test is a simple response status check.
    def test_list_get(self):
        url = reverse('images-list')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    
class CommentsViewSetTestCase(APITestCase):

    def test_list_get(self):
        image_1 = Image.objects.create(name='Test image', img=os.path.join(MEDIA_ROOT, 'test.jpg'))
        comment_1 = Comment.objects.create(img=image_1, text='First comment test text')
        comment_2 = Comment.objects.create(img=image_1, text='Second comment test text')
        url = reverse ('comments-list')
        response = self.client.get(url)
        serializer_data = CommentsSerializer([comment_1, comment_2], many=True).data
        self.assertEqual(serializer_data, response.data['results'])