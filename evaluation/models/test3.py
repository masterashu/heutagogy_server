from django.db import models
from .base import GeneralTest
from django.core.exceptions import ValidationError
import re


def validate_number_list(value):
    if re.fullmatch(r'[\d\s]+', value) is None:
        return ValidationError('The number representation is not correct')


class NumberList(models.Model):
    numbers = models.CharField(max_length=100, null=False, blank=False)
    test = models.ForeignKey('Test3', on_delete=models.CASCADE)

    def get_numbers(self):
        return list(map(int, self.numbers.split()))


class Test3(GeneralTest):
    heading = models.CharField(max_length=40, verbose_name='Heading Text(Optional)', null=True, blank=True)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Number Ordering Puzzle"

    def __str__(self):
        return self.name
