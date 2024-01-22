from django.db import models


class Person(models.Model):
    forename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.forename} {self.lastname} {self.address}"
