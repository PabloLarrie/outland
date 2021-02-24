from django.db import models

class Core(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

class Root(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

class Secondary(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

class Periphery(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

class Special(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
