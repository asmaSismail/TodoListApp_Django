from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class Task (models.Model):
    STATUS = (('done','DONE'), ('processed', 'PROCESSED'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=50,null=False,blank=False)
    description = models.CharField(max_length=200,null = True , blank=True)
    status=models.CharField(choices=STATUS, max_length=10,default='processed')
    date=models.DateField(default=timezone.now)

    def __str__(self):
         return f'{self.date} -> {self.title} : {self.description} / {self.status}' 
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'title'], name='unique_user_task'),
        ] 