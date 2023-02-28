from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import managers


class CustomUser(AbstractUser):
    """
    A User model that uses `email` as it's default identifier instead of
    username.
    """

    username = None
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField()
    gender = models.CharField(
        max_length=140,
        null=True,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        )
    )
    birth_date = models.DateField(null=True, blank=True)
    pro = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.CustomUserManager()

    def __str__(self):
        return self.email
    
class Test(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    descriptor = models.CharField(max_length=255, db_index=True)
    score = models.FloatField()
    date_taken = models.DateTimeField()
    def __str__(self):
        return self.name
    
    def formatted_date_taken(self):
        return self.date_taken.strftime('%Y-%m-%d %H:%M:%S')


class Question(models.Model):
    title = models.CharField(max_length=255)
    q1 = models.CharField(max_length=255)
    q2 = models.CharField(max_length=255)
    q3 = models.CharField(max_length=255)
    q4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    test = models.ForeignKey(Test, related_name='questions',on_delete=models.CASCADE)
        
    def __str__(self) -> str:
        return self.title
    
class UserTest(models.Model):
    user = models.ForeignKey(CustomUser, related_name='exams', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)



