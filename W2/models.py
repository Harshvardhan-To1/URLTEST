from django.db import models
class Present(models.Model):
    Roll_No = models.TextField(max_length = 122)
    Password= models.TextField(max_length = 122)
    Date = models.DateField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    def __str__(self):
        return self.Roll_No
# Create your models here.
