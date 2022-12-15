from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255)
    q1 = models.CharField(max_length=255)
    q2 = models.CharField(max_length=255)
    q3 = models.CharField(max_length=255)
    q4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=255)
    question = models.ForeignKey(Question, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
