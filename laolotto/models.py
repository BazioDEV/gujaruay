from django.db import models

class lao_vip(models.Model):
    title = models.CharField(max_length=20)
    Five = models.CharField(max_length=20)
    Four = models.CharField(max_length=20)
    Three = models.CharField(max_length=20)
    Two = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    
    def __str__(self):
        return self.date
    
class lao_lotto(models.Model):
    title = models.CharField(max_length=20)
    Four = models.CharField(max_length=20)
    Three = models.CharField(max_length=20)
    Two = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    
    def __str__(self):
        return self.date

    