from unittest import result
from django.test import TestCase
from django.shortcuts import resolve_url


from register_car.forms import RegisterCarForms
from register_car.models import RegisterCar


class TestViewsUsingRoutesAndReturningTemplatesHtml(TestCase):

    def setUp(self) -> None:
        self.response = self.client.get(resolve_url('registercar'))

    def test_route_returning_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_route_returning_is_valid_template_register_car_html(self):
        self.assertTemplateUsed(self.response, 'register_car.html')
    
    def test_route_returning_is_valid_view_in_template_register_car_html(self):
        response_template = self.client.get(resolve_url('/registercar/view'))
        self.assertTemplateUsed(response_template, 'register_car.html')

    def test_route_returning_is_valid_update_in_template_register_car_html(self):
        response_template = self.client.get(resolve_url('/registercar/update'))
        self.assertTemplateUsed(response_template, 'register_car.html')

    def test_route_returning_is_valid_delete_in_template_register_car_html(self):
        response_template = self.client.get(resolve_url('/registercar/delete'))
        self.assertTemplateUsed(response_template, 'register_car.html')


    def test_route_returning_is_valid_new_car_in_template_register_car_form_html(self):
        response_template = self.client.get(resolve_url('/registercar/new'))
        self.assertTemplateUsed(response_template, 'register_car_form.html')
    

class TestViewsReturningRouteTemplate(TestCase):
    def setUp(self) -> None:
        register = RegisterCar.objects.create(name='test', type_car='test',plaque='test', value=700)
        register.save()
    
    def test_create(self):
        self.assertTrue(RegisterCar.objects.exists)

    def test_route_view_returning_status_code_200(self):
        response_get = self.client.get('/registercar/view')
        self.assertEqual(response_get.status_code, 200)

    def test_route_create_returning_status_code_200(self):
        response_get = self.client.get('/registercar/new')
        self.assertEqual(response_get.status_code, 200)
    
    def test_route_update_returning_status_code_200(self):
        result = RegisterCar.objects.last()
        response_get = self.client.get(f'/registercar/update/{result.id}')
        self.assertEqual(response_get.status_code, 200)

    def test_route_delete_returning_status_code_302(self):
        result = RegisterCar.objects.last()
        response_get = self.client.get(f'/registercar/delete/{result.id}')
        self.assertEqual(response_get.status_code, 302)



