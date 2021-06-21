from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="qna/", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:3]