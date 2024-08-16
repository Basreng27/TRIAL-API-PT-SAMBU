from django.db import models

# Create your models here.
class Number(models.Model):
    num1 = models.BigIntegerField()
    num2 = models.BigIntegerField()
    random_number = models.BigIntegerField()

    def __str__(self):
        return f"Number(num1={self.num1}, num2={self.num2})"