from django.db import models
from datetime import date

# Create your models here.
class Game(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(blank=True, max_length=127)
    name = models.CharField(max_length=127)

    def __unicode__(self):
        return "%s: %s" % (self.date, self.name)
        
    class Meta:
        ordering = ['time']
