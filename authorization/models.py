from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    password = models.CharField(max_length=300)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.second_name


class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=70)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.profession + ' ' + str(self.user)
