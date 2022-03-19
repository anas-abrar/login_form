from django.db import models

# Create your models here.
class AccountUser(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=30)
    user_password=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.user_name}'
