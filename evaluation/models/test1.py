from django.db import models
from .base import GeneralTest


class Option(models.Model):
    # This model Defines a Multiple Correct Options Question Choices
    text = models.CharField(max_length=50, verbose_name='Option')
    correct = models.BooleanField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Question(models.Model):
    # This model Defines a Multiple Correct Options Question
    test = models.ForeignKey('Test1', on_delete=models.CASCADE)
    text = models.CharField(max_length=200, verbose_name='Question')

    class Meta:
        verbose_name = "Multiple Choice Question"

    def __str__(self):
        return self.text


class Test1(GeneralTest):
    # This model Defines a Multiple Correct Options Test
    heading = models.CharField(max_length=40, verbose_name='Heading Text(Optional)', null=True, blank=True)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Multiple Choice Test"

    def __str__(self):
        return self.heading
