# Generated by Django 3.1.5 on 2021-02-22 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveObjectsManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'CompanyAddress',
            },
        ),
        migrations.CreateModel(
            name='EmployeeAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'EmployeeAddress',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('passport_seria', models.CharField(max_length=2)),
                ('passport_seria_number', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Seria Number')),
                ('specialist', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='company.employeeaddress')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Production', 'Production'), ('Service', 'Service'), ('Sale', 'Sale')], max_length=200, null=True)),
                ('company_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('reception_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='company.companyaddress')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
