from django.contrib.auth.models import AbstractUser


class Accounts(AbstractUser):
    class Meta:
        db_table = 'accounts'
