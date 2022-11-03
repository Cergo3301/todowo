from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    task = models.TextField(max_length=500, blank=True, verbose_name='Описание задачи')
    important = models.BooleanField(default=False, verbose_name='Это важно')
    datecompleted = models.DateTimeField(null=True, blank=True, verbose_name='Дата выполнения')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title