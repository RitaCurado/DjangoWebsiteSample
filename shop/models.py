# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    image = models.ImageField()
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

class Category(models.Model):
    name = models.CharField(max_length=200)