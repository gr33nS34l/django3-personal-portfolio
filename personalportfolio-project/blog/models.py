from django.db import models
import datetime

class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    text = models.TextField()

# For showing the name in the admin panel
    def __str__(self):
        return self.title