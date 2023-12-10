from django.db import models


class Book(models.Model):

    title = models.CharField(
        verbose_name='Title',
        max_length=150
    )
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='images/', verbose_name='Image', null=True)

    def __str__(self) -> str:
        return f'Titulo: {self.title}  Description {self.description}'
    
    def delete(self, using=None , keep_parente=False):
        self.image.storage.delete(self.image.name)
        super().delete()