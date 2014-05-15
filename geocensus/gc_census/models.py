from django.contrib.gis.db import models


class CensusReport(models.Model):
    STRUCTURE_TYPE_CHOICES = (
        ('SINGLE_DETACHED', 'Single Detached'),
        ('SEMI_DETACHED', 'Semi Detached'),
        ('ROW_HOUSE', 'Row House'),
        ('APT_DUPLEX', 'Apartment in Duplex'),
        ('APT_MORE_5F', 'Apartment in Building With 5 Or More Floors'),
        ('APT_LESS_5F', 'Apartment in Building With Less Than 5 Floors'),
        ('SINGLE_ATTACHED', 'Single Attached'),
        ('MOBILE_HOME', 'Mobile Home'),
        ('MOVABLE_HOME', 'Movable Home'),
    )

    create_date = models.DateField()
    structure_type = models.CharField(max_length=100, choices=STRUCTURE_TYPE_CHOICES)
    annual_income = models.DecimalField(max_digits=12, decimal_places=2)
    latitude = models.FloatField()
    longitude = models.FloatField()
    point = models.PointField()


class Person(models.Model):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    EMPLOYMENT_CHOICES = (
        ('UN', 'Unemployed'),
        ('ML', 'Manual Labor'),
        ('PR', 'Professional'),
        ('SE', 'Self-Employed'),
        ('BO', 'Business Owner'),
        ('ST', 'Student'),
        ('RE', 'Retired'),
    )

    census_report = models.ForeignKey('CensusReport')
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    employment_status = models.CharField(max_length=100, choices=EMPLOYMENT_CHOICES)