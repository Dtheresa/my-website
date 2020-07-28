from django.conf import settings
from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.CharField(max_length=250)
    book_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=50)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)

    def status(self):
        self.end_date = timezone.now()
        self.save()

    def __str__(self):
        return self.book_title


