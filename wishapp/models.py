from django.db import models
from django.contrib.auth.models import User



class Wish(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    name = models.CharField(max_length = 100)
#    description = models.TextField()
    url = models.TextField(null=True, blank=True) #were made optional for testing
    image = models.ImageField(null=True, blank=True)
#    check = models.booleanField(default=False)
    def __str__(self):
        return self.name
