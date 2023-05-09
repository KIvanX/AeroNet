from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=70)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.profession + ' ' + str(self.user)
