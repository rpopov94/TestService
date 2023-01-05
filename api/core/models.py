from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Test(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self) -> str:
        return self.title



class Question(models.Model):
    title = RichTextUploadingField()
    q1 = models.CharField(max_length=255)
    q2 = models.CharField(max_length=255)
    q3 = models.CharField(max_length=255)
    q4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    test = models.ForeignKey(Test, related_name='questions',on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title


