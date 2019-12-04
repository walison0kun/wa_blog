from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    resumo = RichTextField()
    conteudo = RichTextUploadingField()
    dt_cri_post = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    #dt_pub_post = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    def snippet(self):
        return self.resumo[:200] +'...'
