from django.db import models
import datetime
from django.utils.text import slugify
from account.models import InstructorProfile, MyUser


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    descriptions = models.TextField()
    created = models.DateField()

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=75)
    descriptions = models.TextField()
    start_time = models.DateField(default=datetime.date.today())
    end_time = models.DateField()
    capacity = models.IntegerField()
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    student = models.ManyToManyField(MyUser)
    slug = models.SlugField(null=True, blank=True)
    view = models.IntegerField(default=0)
    created_at = models.DateField()
    is_active = models.BooleanField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save()

    def __str__(self):
        return self.title
