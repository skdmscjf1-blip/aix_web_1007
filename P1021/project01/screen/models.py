from django.db import models

class Screen(models.Model) :
    sno = models.AutoField(primary_key=True)
    rank = models.IntegerField(default=0)
    title = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True,blank=True)
    percent = models.FloatField(default=0)
    revenue = models.IntegerField(default=0)
    crevenue = models.IntegerField(default=0)
    sales = models.IntegerField(default=0)
    csales = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.sno},{self.rank},{self.title},{self.date},{self.percent},{self.revenue},{self.crevenue},{self.sales},{self.csales},'
