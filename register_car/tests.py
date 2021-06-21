from register_car.models import RegisterCar
from django.test import TestCase


class TestViews(TestCase):

    def setUp(self) -> None:
        register_car = RegisterCar.objects.create(
            name='TestName', type_car='TestType', plaque='TestPlaque', value=700)
        register_car.save()
        self.response_get = self.client.get('/registercar/list')
    
    def test_route_list_all_returning_status_code(self):
        self.assertEqual(self.response_get.status_code, 200)
    
    def test_route_list_all_returning_is_valid_template(self):
        self.assertTemplateUsed(self.response_get, 'register_car_view.html')