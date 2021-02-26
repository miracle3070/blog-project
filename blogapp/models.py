from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=50, default="Unknown")
    image = models.ImageField(upload_to="image/", null=True, blank=True, default="null")
    content = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:50]

class Comment(models.Model):
    post_id = models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE, db_column="post_id")
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.author + " - " + str(self.pub_date)