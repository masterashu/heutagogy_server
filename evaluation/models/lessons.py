from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=40, verbose_name='Lesson Title')
    study_text = models.CharField(max_length=1000, verbose_name='Lesson Study Material')
