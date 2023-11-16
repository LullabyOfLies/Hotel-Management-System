from django.db import models

class Admins(models.Model):
    email = models.EmailField()
    username = models.CharField("Name", max_length=240)
    last_name = models.CharField("Last Name", max_length=240)
    first_name = models.CharField("First Name", max_length=240)
    middle_name = models.CharField("Middle Name", max_length=240)

    def __str__(self):
        return self.username