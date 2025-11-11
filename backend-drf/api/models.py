from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} - {self.date}"

