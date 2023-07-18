from django.db import models
from datetime import datetime

class Book(models.Model):
    
    CATEGORY_OPTIONS = [
        ("CRIME", "Crime"),
        ("CIÊNCIA", "Ciência"),
        ("DRAMA", "Drama"),
        ("FANTASIA", "Fantasia"),
        ("FICÇÃO CIENTÍFICA", "Ficção Científica"),
        ("MISTÉRIO", "Mistério"),
        ("AUTORES NACIONAIS", "Autores Nacionais"),
        ("ROMANCE", "Romance"),
        ("ROMANCE DE ÉPOCA","Romance de Época"),
        ("SUSPENSE", "Suspense"),
        ("TERROR", "Terror"),
    ]

    title = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS, default='')
    synopsis = models.TextField(null=False, blank=False)
    date = models.DateTimeField(default=datetime.now, blank=False)
    cover = models.ImageField(upload_to="%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.title