from django.db import models
from .managers import GeneralManager


class Rain(models.Model):
    amount = models.IntegerField()
    date = models.DateField(auto_now=False)
    objects = models.Manager()
    my_query = GeneralManager()


    class Meta:
        ordering = ['date']

    def __str__(self):
        return "{}mm of rain fell on {}".format(self.amount, self.date)
