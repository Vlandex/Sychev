from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

class Post(models.Model): 
    # Тип: TextField
    header = models.CharField(max_length=200)
    text = models.TextField() 
    # Тип поля: DateTimeField, для хранения даты и времени;
    # параметр auto_now_add определяет, что в поле будет автоматически
    # подставлено время и дата создания новой записи
    pub_date = models.DateTimeField(auto_now_add=True)
    # Тип: ForeignKey, ссылка на модель User
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    ) 
# Create your models here.
