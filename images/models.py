from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField()
    date_upload = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    size = models.IntegerField(editable=False)
    def save(self, *args, **kwargs):
        self.size = self.img.size
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

#Uses many-to-one relationship, meaning multiple comments are possible for 1 image. Can be changed to one-to-one if needed.
class Comment(models.Model):
    img = models.ForeignKey('Image', on_delete=models.CASCADE, related_name='comments') 
    text = models.TextField(max_length=100)
    date_post = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text