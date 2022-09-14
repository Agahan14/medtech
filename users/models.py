from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone


class SuperUser(BaseUserManager):
    def create_user(self, username, email, **extra_fields):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.user_type = 'admin'
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    objects = SuperUser()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'System user'
        verbose_name_plural = "System users"


class UserForInheritance(User):
    image = models.TextField(null=True, blank=True)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class OfficeManager(UserForInheritance):
    pass


class Patient(UserForInheritance):
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    date_of_pregnancy = models.DateField(auto_now_add=False)
    inn = models.CharField(max_length=14, unique=True)
    doctor_field = models.ForeignKey('Doctor', on_delete=models.PROTECT, related_name='patient')


class Doctor(UserForInheritance):
    resign = models.TextField(blank=True)
    education = models.TextField(blank=True)
    professional_sphere = models.TextField(blank=True)
    work_experience = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
