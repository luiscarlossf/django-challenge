from django.test import TestCase

from api.models import RegularPlan
from random import uniform, choice, randint

class RegularPlanModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        RegularPlan.objects.create(
            name='RegularPlan1',
            tar_included=choice([True, False]),
            subscription=uniform(1, 2000),
            cycle=choice(RegularPlan.CYCLE_CHOICES)[0],
            type=choice(RegularPlan.TYPE_CHOICES)[0],
            offer_iva=choice([True, False]),
            off_peak_price=uniform(100, 2000),
            peak_price=uniform(2000,2500),
            unit=choice(RegularPlan.UNIT_CHOICES)[0],
            valid=choice([True, False]),
            publish=choice([True, False]),
            vat=randint(1, 100)
        )
    
    def test_name_label(self):
        plan = RegularPlan.objects.get(id=1)
        field_label = plan._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Name')
    
    def test_tar_included_label(self):
        plan = RegularPlan.objects.get(id=1)
        field_label = plan._meta.get_field('tar_included').verbose_name
        self.assertEquals(field_label, 'Tar Included')
    
    def test_subscription_label(self):
        plan = RegularPlan.objects.get(id=1)
        field_label = plan._meta.get_field('subscription').verbose_name
        self.assertEquals(field_label, 'Subscription')
    
    def test_cycle_label(self):
        plan = RegularPlan.objects.get(id=1)
        field_label = plan._meta.get_field('cycle').verbose_name
        self.assertEquals(field_label, 'Cycle')
    
    def test_type_label(self):
        plan = RegularPlan.objects.get(id=1)
        field_label = plan._meta.get_field('type').verbose_name
        self.assertEquals(field_label, 'Type')
    
    def test_offer_iva_label(self):
        plan = RegularPlan.objects.get(id=1)
        field_label = plan._meta.get_field('offer_iva').verbose_name
        self.assertEquals(field_label, 'Offer IVA')
    
    def test_off_peak_price_label(self):
        plan = RegularPlan.objects.get(id=1)
        field_label = plan._meta.get_field('off_peak_price').verbose_name
        self.assertEquals(field_label, 'Off Peak Price')
    
    def test_peak_price_label(self):
        plan = RegularPlan.objects.get(id=1)
        field_label = plan._meta.get_field('peak_price').verbose_name
        self.assertEquals(field_label, 'Peak Price')

    def test_unit_label(self):
        plan = RegularPlan.objects.get(id=1)
        field_label = plan._meta.get_field('unit').verbose_name
        self.assertEquals(field_label, 'Unit')

    def test_valid_label(self):
        plan = RegularPlan.objects.get(id=1)
        field_label = plan._meta.get_field('valid').verbose_name
        self.assertEquals(field_label, 'Valid')
    
    def test_publish_label(self):
        plan = RegularPlan.objects.get(id=1)
        field_label = plan._meta.get_field('publish').verbose_name
        self.assertEquals(field_label, 'Publish')
    
    def test_vat_label(self):
        plan = RegularPlan.objects.get(id=1)
        field_label = plan._meta.get_field('vat').verbose_name
        self.assertEquals(field_label, 'Vat')
    
    def test_owner_label(self):
        plan = RegularPlan.objects.get(id=1)
        field_label = plan._meta.get_field('owner').verbose_name
        self.assertEquals(field_label, 'owner')
    
    def test_name_max_length(self):
        plan = RegularPlan.objects.get(id=1)
        max_length = plan._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)
    
    def test_cycle_max_length(self):
        plan = RegularPlan.objects.get(id=1)
        max_length = plan._meta.get_field('cycle').max_length
        self.assertEquals(max_length, 2)
    
    def test_type_max_length(self):
        plan = RegularPlan.objects.get(id=1)
        max_length = plan._meta.get_field('type').max_length
        self.assertEquals(max_length, 2)
    
    def test_unit_max_length(self):
        plan = RegularPlan.objects.get(id=1)
        max_length = plan._meta.get_field('unit').max_length
        self.assertEquals(max_length, 3)
    
    def test_vat_min_value(self):
        plan = RegularPlan.objects.get(id=1)
        min_value = plan._meta.get_field('vat').validators[0].__getattribute__('limit_value')
        self.assertEquals(min_value, 1)
    
    def test_vat_min_value(self):
        plan = RegularPlan.objects.get(id=1)
        max_value = plan._meta.get_field('vat').validators[1].__getattribute__('limit_value')
        self.assertEquals(max_value, 100)
    
    def test_cycles_choices_value(self):
        DAILY = 'DD'
        WEEKLY = 'WK'
        WAITED_CYCLE_CHOICES = [
            (DAILY, 'Daily'),
            (WEEKLY, 'Weekly'),
        ]
        self.assertEquals(WAITED_CYCLE_CHOICES, RegularPlan.CYCLE_CHOICES)
    
    def test_type_choices_value(self):
        BI_TIME = 'BT'
        TRI_TIME = 'TT'
        SIMPLE = 'ST'
        WAITED_TYPE_CHOICES = [
            (BI_TIME, 'Bi-Time'),
            (TRI_TIME, 'Tri-Time'),
            (SIMPLE, 'Simple'),
        ]
        self.assertEquals(WAITED_TYPE_CHOICES, RegularPlan.TYPE_CHOICES)
    
    def test_cycles_choices_value(self):
        KILOMETERS = 'KWH'
        MINUTES = 'MIN'
        WAITED_UNIT_CHOICES = [
            (KILOMETERS, "Kilometers/hour"),
            (MINUTES, "Minutes")
        ]
        self.assertEquals(WAITED_UNIT_CHOICES, RegularPlan.UNIT_CHOICES)