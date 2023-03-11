from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Country(models.Model):
    name_country = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.name_country}'


class City(models.Model):
    name_city = models.CharField(max_length=70)
    country = models.ForeignKey(Country , on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.name_city}'


class University(models.Model):
    RATE_ADMISSION = [(str(i),i) for i in range(1,300)]
    city = models.ForeignKey(City , on_delete = models.CASCADE)
    name = models.CharField(max_length=60)
    acronym = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='covers/')
    type = models.CharField(max_length=20)
    overview = models.TextField()
    year_university = models.DateField()
    numbers_students = models.PositiveIntegerField(default=0)
    numbers_national_students = models.PositiveIntegerField(default=0)
    address_site = models.TextField()
    rate_admission = models.CharField(choices=RATE_ADMISSION , max_length=15)


    def __str__(self):
        return f'{self.name}: {self.address_site}'

