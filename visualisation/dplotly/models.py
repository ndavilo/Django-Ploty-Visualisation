from django.db import models

# Create your models here.

class BTC(models.Model):
    Date    = models.DateField()
    Open    = models.FloatField()
    High    = models.FloatField()
    Low     = models.FloatField()
    Close   = models.FloatField()
    AdjClose= models.FloatField()
    Volume  = models.FloatField()

    def __str__(self):
        return str(self.Date)
    class Meta:
        ordering = ('Date',) 

class BNB(models.Model):
    Date    = models.DateField()
    Open    = models.FloatField()
    High    = models.FloatField()
    Low     = models.FloatField()
    Close   = models.FloatField()
    AdjClose= models.FloatField()
    Volume  = models.FloatField()

    def __str__(self):
        return str(self.Date)
    class Meta:
        ordering = ('Date',) 

class ETH(models.Model):
    Date    = models.DateField()
    Open    = models.FloatField()
    High    = models.FloatField()
    Low     = models.FloatField()
    Close   = models.FloatField()
    AdjClose= models.FloatField()
    Volume  = models.FloatField()

    def __str__(self):
        return str(self.Date)
    class Meta:
        ordering = ('Date',)
