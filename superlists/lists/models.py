# -*-coding:utf-8-*-
from django.db import models

# Create your models here.


class Item(models.Model):
    """docstring for Item"""
    text = models.TextField(default='')

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        pass
