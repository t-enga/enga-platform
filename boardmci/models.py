from django.db import models

# Create your models here.

class Mci(models.Model):
    id_mci=models.AutoField(primary_key=True)
    mci_name=models.CharField(max_length=150,null=True, blank=True)
    mci_active=models.BooleanField(default=False, null=True, blank=True)
    def __str__(self):
        return self.mci_name
    
class Mdp(models.Model):
    id_mdp=models.AutoField(primary_key=True)
    id_mci=models.ForeignKey(Mci,null=True, blank=True, on_delete=models.DO_NOTHING)
    mdp_name=models.CharField(max_length=150,null=True, blank=True)
    mdp_active=models.BooleanField(default=None,null=True, blank=True)
    def __str__(self):
        return self.mdp_name
    
class Part(models.Model):
    id_part=models.AutoField(primary_key=True,)
    week_num=models.IntegerField(null=True, blank=True)
    name_part=models.CharField(max_length=30,null=True, blank=True)
    cal_day1=models.IntegerField(null=True, blank=True)
    cal_day2=models.IntegerField(null=True, blank=True)
    cal_day3=models.IntegerField(null=True, blank=True)
    cal_day4=models.IntegerField(null=True, blank=True)
    cal_day5=models.IntegerField(null=True, blank=True)
    cal_day6=models.IntegerField(null=True, blank=True)
    cal_day7=models.IntegerField(null=True, blank=True)
    prom_wek=models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name_part + ' Semana ' + self.week_num