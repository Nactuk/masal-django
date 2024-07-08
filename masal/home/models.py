from django.db import models

# Create your models here.

class Masal(models.Model):
    name = models.CharField(max_length=100, verbose_name= ('Masal adi'))
    description = models.TextField(verbose_name='Masal aciklamasi')
    content = models.TextField(verbose_name='Masal icerigi')
    image = models.CharField(max_length=50, verbose_name='Fotografinin ismi')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Eklendigi tarih')
    isPublished = models.BooleanField(default=True,verbose_name='Yayinda')
    def __str__(self):
        return self.name
