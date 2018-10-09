from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    textField = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name=True)

