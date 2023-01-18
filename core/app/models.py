from django.db import models

# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=200)
    q_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - ({str(self.q_date.time())})"
    
class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    total_votes=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - ({self.question.title})"
    
    