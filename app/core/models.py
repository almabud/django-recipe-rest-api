from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, password=password, **extra_fields)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        user = self.model(email=email, password=password)
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        def normalize_email(email):
            """
            Normalize the address by lowercasing the domain part of the email
            address.
            """
            email = email or ''
            try:
                email_name, domain_part = email.strip().rsplit('@', 1)
            except ValueError:
                pass
            else:
                email = '@'.join([email_name, domain_part.lower()])
            return email
        if not self.email:
            raise ValueError("Email is required")
        self.email = normalize_email(self.email)
        self.set_password(self.password)
        super(User, self).save(*args, **kwargs)
