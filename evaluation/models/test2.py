from django.db import models
from .base import GeneralTest


class PictureDescriptionPair(models.Model):
    picture = models.ImageField()
    description = models.TextField(max_length=100, verbose_name='Image Description')
    test = models.ForeignKey('Test2', on_delete=models.CASCADE)


class Test2(GeneralTest):
    # This is a Matching Game for pictures and Description
    heading = models.CharField(max_length=40, verbose_name='Heading Text(Optional)', null=True, blank=True)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='test2')

    class Meta:
        verbose_name = "Pictures & Description Matching Game"

    def __str__(self):
        return str(self.name)
