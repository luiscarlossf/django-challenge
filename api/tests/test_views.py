from django.test import TestCase
from django.conf import settings
from api.models import RegularPlan
from django.contrib.auth.models import User
from random import uniform, choice, randint

class RegularPlanViewsetListView(TestCase):
    
    def setUp(self):
        #Number of regular plans for page
        number_of_plans = 10

        superuser = User.objects.create(username='miiotest', password='290#@$s145', is_superuser=True)

        # Create number_of_plans RegularPlan objects
        for plan_id in range(number_of_plans):
            RegularPlan.objects.create(
                name=f'RegularPlan {plan_id}',
                tar_included=choice([True, False]),
                subscription=uniform(1, 2000),
                cycle=choice(RegularPlan.CYCLE_CHOICES)[0],
                type=choice(RegularPlan.TYPE_CHOICES)[0],
                offer_iva=choice([True, False]),
                off_peak_price=uniform(100, 2000),
                peak_price=uniform(2000,2500),
                unit=choice(RegularPlan.UNIT_CHOICES)[0],
                valid=choice([True, False]),
                publish=True,
                vat=randint(1, 100),
            )
        
        #Create two users
        user1 = User.objects.create_user(username='user1', password='390290#$($')
        user2 = User.objects.create_user(username='user2', password='#$3d232434')
         
        user1.save()
        user2.save()

        RegularPlan.objects.create(
            name='RegularPlan User1',
            tar_included=choice([True, False]),
            subscription=uniform(1, 2000),
            cycle=choice(RegularPlan.CYCLE_CHOICES)[0],
            type=choice(RegularPlan.TYPE_CHOICES)[0],
            offer_iva=choice([True, False]),
            off_peak_price=uniform(100, 2000),
            peak_price=uniform(2000,2500),
            unit=choice(RegularPlan.UNIT_CHOICES)[0],
            valid=choice([True, False]),
            publish=False,
            vat=randint(1, 100),
            owner=user1,
        )
        RegularPlan.objects.create(
            name='RegularPlan User2',
            tar_included=choice([True, False]),
            subscription=uniform(1, 2000),
            cycle=choice(RegularPlan.CYCLE_CHOICES)[0],
            type=choice(RegularPlan.TYPE_CHOICES)[0],
            offer_iva=choice([True, False]),
            off_peak_price=uniform(100, 2000),
            peak_price=uniform(2000,2500),
            unit=choice(RegularPlan.UNIT_CHOICES)[0],
            valid=choice([True, False]),
            publish=False,
            vat=randint(1, 100),
            owner=user2,
        )
    
    def test_router_list_exists_at_desired_location(self):
        response = self.client.get('/api/plans/')
        self.assertEquals(response.status_code, 200)
    
    def test_router_create_exists_at_desired_location(self):
        login = self.client.login(username='user1', password='390290#$($')
        data = { 
            'name':'RegularPlan -1',
            'tar_included':choice([True, False]),
            'subscription':uniform(1, 2000),
            'cycle':choice(RegularPlan.CYCLE_CHOICES)[0],
            'type':choice(RegularPlan.TYPE_CHOICES)[0],
            'offer_iva':choice([True, False]),
            'off_peak_price':uniform(100, 2000),
            'peak_price':uniform(2000,2500),
            'unit':choice(RegularPlan.UNIT_CHOICES)[0],
            'valid':choice([True, False]),
            'publish':False,
            'vat':randint(1, 100),
        }
        response = self.client.post('/api/plans/', data=data, content_type="application/json")
        self.assertEquals(response.status_code, 201)
    
    def test_router_update_exists_at_desired_location(self):
        login = self.client.login(username='user1', password='390290#$($')
        data = { 
            'name':'RegularPlan -1',
            'tar_included':choice([True, False]),
            'subscription':uniform(1, 2000),
            'cycle':choice(RegularPlan.CYCLE_CHOICES)[0],
            'type':choice(RegularPlan.TYPE_CHOICES)[0],
            'offer_iva':choice([True, False]),
            'off_peak_price':uniform(100, 2000),
            'peak_price':uniform(2000,2500),
            'unit':choice(RegularPlan.UNIT_CHOICES)[0],
            'valid':choice([True, False]),
            'publish':False,
            'vat':randint(1, 100),
        }
        user = User.objects.get(username='user1')
        plan=RegularPlan.objects.get(owner=user)
        response = self.client.put(f'/api/plans/{plan.pk}/', data=data, content_type="application/json")
        self.assertEquals(response.status_code, 200)
    
    def test_router_list_by_user_exists_at_desired_location(self):
        login = self.client.login(username='user1', password='390290#$($')
        response = self.client.get('/api/plans/list_by_user/')
        self.assertEquals(response.status_code, 200)
    
    def test_lists_all_plans(self):
        response = self.client.get('/api/plans/')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(len(response.data), 10)

    def test_create_plan(self):
        login = self.client.login(username='user1', password='390290#$($')
        data = { 
            'name':'RegularPlan Created',
            'tar_included':choice([True, False]),
            'subscription':uniform(1, 2000),
            'cycle':choice(RegularPlan.CYCLE_CHOICES)[0],
            'type':choice(RegularPlan.TYPE_CHOICES)[0],
            'offer_iva':choice([True, False]),
            'off_peak_price':uniform(100, 2000),
            'peak_price':uniform(2000,2500),
            'unit':choice(RegularPlan.UNIT_CHOICES)[0],
            'valid':choice([True, False]),
            'publish':False,
            'vat':randint(1, 100),
        }
        response = self.client.post('/api/plans/', data=data, content_type="application/json")
        self.assertEquals(response.status_code, 201)
        response = self.client.get('/api/plans/list_by_user/')
        self.assertTrue(len(response.data), 2)
    
    
    def test_update_plan(self):
        login = self.client.login(username='user1', password='390290#$($')
        data = { 
            'name':'RegularPlan Updated',
            'tar_included':choice([True, False]),
            'subscription':uniform(1, 2000),
            'cycle':choice(RegularPlan.CYCLE_CHOICES)[0],
            'type':choice(RegularPlan.TYPE_CHOICES)[0],
            'offer_iva':choice([True, False]),
            'off_peak_price':uniform(100, 2000),
            'peak_price':uniform(2000,2500),
            'unit':choice(RegularPlan.UNIT_CHOICES)[0],
            'valid':choice([True, False]),
            'publish':False,
            'vat':randint(1, 100),
        }
        user = User.objects.get(username='user1')
        plan=RegularPlan.objects.get(owner=user)
        response = self.client.put(f'/api/plans/{plan.pk}/', data=data, content_type="application/json")
        self.assertEquals(response.data['name'], 'RegularPlan Updated')
        self.assertEquals(response.status_code, 200)
        
    
    def test_lists_plans_by_user(self):
        login = self.client.login(username='user1', password='390290#$($')
        response = self.client.get('/api/plans/list_by_user/')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(len(response.data), 1)

    def test_create_permissions(self):
        data = { 
            'name':'RegularPlan Created',
            'tar_included':choice([True, False]),
            'subscription':uniform(1, 2000),
            'cycle':choice(RegularPlan.CYCLE_CHOICES)[0],
            'type':choice(RegularPlan.TYPE_CHOICES)[0],
            'offer_iva':choice([True, False]),
            'off_peak_price':uniform(100, 2000),
            'peak_price':uniform(2000,2500),
            'unit':choice(RegularPlan.UNIT_CHOICES)[0],
            'valid':choice([True, False]),
            'publish':False,
            'vat':randint(1, 100),
        }
        response = self.client.post('/api/plans/', data=data, content_type="application/json")
        self.assertEquals(response.status_code, 403)
        login = self.client.login(username='user1', password='390290#$($')
        response = self.client.post('/api/plans/', data=data, content_type="application/json")
        self.assertEquals(response.status_code, 201)
        response = self.client.get('/api/plans/list_by_user/')
        self.assertTrue(len(response.data), 2)
        self.client.logout()
        response = self.client.post('/api/plans/', data=data, content_type="application/json")
        self.assertEquals(response.status_code, 403)
    
    def test_update_permissions(self):
        data = { 
            'name':'RegularPlan Updated',
            'tar_included':choice([True, False]),
            'subscription':uniform(1, 2000),
            'cycle':choice(RegularPlan.CYCLE_CHOICES)[0],
            'type':choice(RegularPlan.TYPE_CHOICES)[0],
            'offer_iva':choice([True, False]),
            'off_peak_price':uniform(100, 2000),
            'peak_price':uniform(2000,2500),
            'unit':choice(RegularPlan.UNIT_CHOICES)[0],
            'valid':choice([True, False]),
            'publish':False,
            'vat':randint(1, 100),
        }
        user1 = User.objects.get(username='user1')
        user2 = User.objects.get(username='user2')
        plan = RegularPlan.objects.get(owner=user1)
        plan2 = RegularPlan.objects.get(owner=user2)
        response = self.client.put(f'/api/plans/{plan.pk}/', data=data, content_type="application/json")
        self.assertEquals(response.status_code, 403)
        login = self.client.login(username='user1', password='390290#$($')
        response = self.client.put(f'/api/plans/{plan.pk}/', data=data, content_type="application/json")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['name'], 'RegularPlan Updated')
        response = self.client.put(f'/api/plans/{plan2.pk}/', data=data, content_type="application/json")
        self.assertEquals(response.status_code, 401)
        self.client.logout()
        response = self.client.put(f'/api/plans/{plan.pk}/', data=data, content_type="application/json")
        self.assertEquals(response.status_code, 403)
    
    def test_list_plan_by_user_permissions(self):
        response = self.client.get('/api/plans/list_by_user/')
        self.assertEquals(response.status_code, 403)
        login = self.client.login(username='user1', password='390290#$($')
        response = self.client.get('/api/plans/list_by_user/')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(len(response.data), 1)
        self.assertEquals(response.data[0]['name'],'RegularPlan User1')
        self.client.logout()
        login = self.client.login(username='user2', password='#$3d232434')
        response = self.client.get('/api/plans/list_by_user/')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(len(response.data), 1)
        self.assertNotEquals(response.data[0]['name'], 'RegularPlan User1')
        self.client.logout()
        response = self.client.get('/api/plans/list_by_user/')
        self.assertEquals(response.status_code, 403)