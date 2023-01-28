from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Vote(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choice = models.ForeignKey("Choice", on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=200)
    q_date=models.DateTimeField(auto_now_add=True)
    voted_by = models.ManyToManyField(settings.AUTH_USER_MODEL, through=Vote)
    def __str__(self):
        return f"{self.title} - ({str(self.q_date.time())})"

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    title=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.title} - ({self.question.title})"

        