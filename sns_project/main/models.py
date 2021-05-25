from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    reg_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:3]