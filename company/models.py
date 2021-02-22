from django.db import models

import uuid
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser


class ActiveObjectsManager(models.Model):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
        # return super().get_queryset().filter(...)


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CompanyAddress(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "CompanyAddress"

    def __str__(self):
        if self.city:
            return f"{self.city} {self.street}"
        return self.city


class Company(BaseModel):
    CATEGORY = (
                ('Production', 'Production'),
                ('Service', 'Service'),
                ('Sale', 'Sale')
            )
    company_name = models.CharField(max_length=50)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    company_email = models.EmailField(max_length=100, null=True, blank=True)
    reception_phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.OneToOneField(CompanyAddress, on_delete=models.PROTECT, null=True, blank=True)

    # class Meta:
    #     verbose_name_plural = ""

    def __str__(self):
        if self.company_name:
            return f"{self.company_name} {self.category}"
        return self.company_name


# *********************

class EmployeeAddress(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "EmployeeAddress"



def photo_upload_path(instance, filename):
    current_dt = timezone.now()
    return f"employee-photos/{current_dt.strftime('%Y_%m')}/{uuid.uuid4().hex}/{filename}"


class Employee(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    passport_seria = models.CharField(max_length=2)
    passport_seria_number = models.DecimalField(max_digits=10, decimal_places=6, verbose_name="Seria Number" )
    company = models.ForeignKey(Company, related_name="employee", on_delete=models.CASCADE, null=True, blank=True)
    specialist = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.OneToOneField(EmployeeAddress, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        if self.last_name:
            return f"{self.last_name} {self.first_name}"
        return self.first_name


# *****************************************************************************************************
# import uuid
#
# # Create your models here.
# from django.utils import timezone
#
#
# class BaseModel(models.Model):
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#
# class Address(models.Model):
#     country = models.CharField(max_length=150, null=True, blank=True)
#     city = models.CharField(max_length=150, null=True, blank=True)
#     street = models.CharField(max_length=150, null=True, blank=True)
#     zip_code = models.IntegerField(blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.city}  {self.street}'
#
#
# class Company(BaseModel):
#     CATEGORY = (
#         ('Production', 'Production'),
#         ('Service', 'Service'),
#         ('Sale', 'Sale')
#     )
#
#     name = models.CharField(max_length=100, blank=True, null=True)
#     category = models.CharField(max_length=200, null=True, choices=CATEGORY)
#     description = models.CharField(max_length=200, null=True, blank=True)
#     address = models.OneToOneField(Address, on_delete=models.PROTECT, null=True, blank=True)
#
#     def __str__(self):
#         return f'{self.name} ---- Joylashgan manzili ---- {self.address}'
#
#
# def photo_upload_path(instance, filename):
#     current_dt = timezone.now()
#     return f"employee-photos/{current_dt.strftime('%Y_%m')}/{uuid.uuid4().hex}/{filename}"
#
# class Employee(BaseModel):
#     first_name = models.CharField(max_length=150, null=True, blank=True)
#     last_name = models.CharField(max_length=150, null=True, blank=True)
#     specialist = models.CharField(max_length=150, null=True, blank=True)
#     phone = models.IntegerField(null=True, blank=True)
#     # passport_letter = models.CharField(max_length=2, verbose_name="passport letter")
#     # passport_number = models.DecimalField(decimal_places=7, max_digits=10)
#     photo = models.ImageField(upload_to=photo_upload_path, blank=True, null=True)
#     company = models.ManyToManyField(Company, help_text="Qaysi kompaniyaga rezume tashlamoqchisiz")
#     city = models.CharField(max_length=150, null=True, blank=True)
#
#     def __str__(self):
#         if self.last_name:
#             return f'{self.last_name} {self.first_name}'
#         return self.first_name
