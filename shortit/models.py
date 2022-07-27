from django.db import models

# Create your models here.
class Links(models.Model):
    org_link = models.CharField(max_length=250)
    short_link = models.CharField(max_length=50)
    stats = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    # last_visit = models.DateField()

    def __str__(self):
        return f"{self.org_link} ({self.created})"
    
class Reports(models.Model):
    name = models.CharField(max_length=50,verbose_name="نام")
    email = models.EmailField(max_length=120,verbose_name="ایمیل")
    description = models.TextField(verbose_name="توضیحات")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    