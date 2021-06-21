from django.test import TestCase
from django.shortcuts import resolve_url


from register_car.forms import RegisterCarForms
from register_car.models import RegisterCar


class TestViewsGet(TestCase):

    def setUp(self) -> None:
        self.response = self.client.get(resolve_url('registercar'))

    def test_route_list_all_returning_status_code_200(self):
        self.assertEqual(200, self.response.status_code)
    
    def test_route_list_all_returning_is_valid_template(self):
        self.assertTemplateUsed(self.response, 'register_car.html')




class TestViewCreate(TestCase):
    def setUp(self) -> None:
        register_car = dict(name='test', type_car='test', plaque='test', value=700)
        self.response = self.client.post(resolve_url('registercar',register_car))
