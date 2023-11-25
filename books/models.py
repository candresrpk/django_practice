from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=150
    )


# class Book(models.Model):
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE
#     )
#     title = models.CharField(
#         max_length=150
#     )
#     description = models.TextField()
#     image = models.ImageField()