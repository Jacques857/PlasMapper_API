from django.db import models

class Plasmid(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.CharField(max_length=50000)
    sequenceLength = models.IntegerField()
    backbone = models.CharField(max_length=200)
    features = models.CharField(max_length=1500) # a string containing feature names seperated by commas
