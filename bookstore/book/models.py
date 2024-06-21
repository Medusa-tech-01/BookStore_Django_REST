from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_date(value):
    if value > timezone.now().date():
        raise ValidationError("Date cannot be in the future")
    
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(validators=[validate_date])
    isbn = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title