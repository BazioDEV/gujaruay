from django.db import models

class gov_thai(models.Model):
    title = models.CharField(max_length=20)
    FirstPrize = models.CharField(max_length=20)
    ThreeFront = models.CharField(max_length=20)
    ThreeFrontTwo = models.CharField(max_length=20)
    ThreeUnder = models.CharField(max_length=20)
    ThreeUnderTwo = models.CharField(max_length=20)
    TwoUnder = models.CharField(max_length=20)
    date = models.CharField(max_length=30)
        
    def __str__(self):
        return self.title