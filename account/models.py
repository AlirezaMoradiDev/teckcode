from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    date_joined = models.DateField(auto_now_add=True)
    username = models.CharField(
        max_length=15,
        unique=True
    )
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    is_instructor = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "email",
        "is_instructor"
    ]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Skill(models.Model):
    name = models.CharField(max_length=30)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class InstructorProfile(models.Model):
    name = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)
    image = models.ImageField(upload_to='Instructor', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


