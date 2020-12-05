from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

"""Defines the models of database.
"""
class RegularPlan(models.Model):
    """Represents a regular plan.
    """
    DAILY = 'DD'
    WEEKLY = 'WK'
    CYCLE_CHOICES = [
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
    ]
    BI_TIME = 'BT'
    TRI_TIME = 'TT'
    SIMPLE = 'ST'
    TYPE_CHOICES = [
        (BI_TIME, 'Bi-Time'),
        (TRI_TIME, 'Tri-Time'),
        (SIMPLE, 'Simple'),
    ]
    KILOMETERS = 'KWH'
    MINUTES = 'MIN'
    UNIT_CHOICES = [
        (KILOMETERS, "Kilometers/hour"),
        (MINUTES, "Minutes")
    ]
    name = models.CharField("Name", help_text="Name of plan", max_length=200)
    tar_included = models.BooleanField("Tar Included")
    subscription = models.FloatField("Subscription", help_text="It's the monthly subscription for the user")
    cycle = models.CharField("Cycle", max_length=2, choices=CYCLE_CHOICES)
    type = models.CharField("Type", max_length=2, choices=TYPE_CHOICES)
    offer_iva = models.BooleanField("Offer IVA")
    off_peak_price = models.FloatField("Off Peak Price")
    peak_price = models.FloatField("Peak Price")
    unit = models.CharField("Unit", max_length=3, choices=UNIT_CHOICES)
    valid = models.BooleanField("Valid")
    publish = models.BooleanField("Publish", help_text="Indicates if plan can be showed to everyone.")
    vat = models.IntegerField("Vat", help_text="Choose a value from 1 to 100.", validators=[
        MinValueValidator(1,'Enter with a value greater than 1 and less than 100'),
        MaxValueValidator(100, 'Enter with a value greater than 1 and less than 100'),
    ])
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )