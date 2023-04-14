from django.db import models

class Tasks(models.Model):
    title = models.CharField('Название', max_length=20)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

