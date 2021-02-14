from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=50, default="Unknown")
    image = models.ImageField(upload_to="image/", null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:50]