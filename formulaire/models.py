from django import forms
from django.db import models

class ContactModel(models.Model):
    Nom= models.CharField(max_length=20)
    Prenom = models.CharField(max_length=20)
    Email= models.CharField(max_length=20)
    Banque= models.CharField(max_length=30)


    def __str__(self):
        return self.Nom