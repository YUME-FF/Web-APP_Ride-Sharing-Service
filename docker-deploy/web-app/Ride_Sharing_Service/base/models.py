from django.db import models

# Create your models here.
class viehcle(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name
    
