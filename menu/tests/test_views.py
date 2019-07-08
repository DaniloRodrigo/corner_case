import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import *
from ..serializers import *
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
import logging
from django.utils import timezone
import datetime
import sys
import os

logger = logging.getLogger(__name__)


client = Client()


class RestaurantsTest(TestCase):

    get_delete_update = 'get_delete_update_restaurant'
    get_post = 'get_post_restaurant'
    obj_serializer = RestaurantSerializer
    obj_class = Restaurant

    def setUp(self):
        self.restaurant1 = self.obj_class.objects.create(title="Restaurant 1")
        self.restaurant2 = self.obj_class.objects.create(title="Restaurant 2")
        self.restaurant3 = self.obj_class.objects.create(title="Restaurant 3")
        self.restaurant4 = self.obj_class.objects.create(title="Restaurant 4")

        self.valid_payload = {
            'title': 'Restaurant 5',
        }
        self.valid_payload_put = {
            'title': 'Restaurant for PUT',
        }
        self.invalid_payload = {
            'title': '',
        }

    def test_get_all(self):
        response = client.get(reverse(self.get_post))
        objs = self.obj_class.objects.all()
        serializer = self.obj_serializer(objs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single(self):
        response = client.get(
            reverse(self.get_delete_update, kwargs={'pk': self.restaurant3.pk}))
        obj = self.obj_class.objects.get(pk=self.restaurant3.pk)
        serializer = self.obj_serializer(obj)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single(self):
        response = client.get(
            reverse(self.get_delete_update, kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid(self):
        response = client.post(
            reverse(self.get_post),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid(self):
        response = client.post(
            reverse(self.get_post),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update(self):
        response = client.put(
            reverse(self.get_delete_update, kwargs={'pk': self.restaurant1.pk}),
            data=json.dumps(self.valid_payload_put),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update(self):
        response = client.put(
            reverse(self.get_delete_update, kwargs={'pk': self.restaurant1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete(self):
        response = client.delete(
            reverse(self.get_delete_update, kwargs={'pk': self.restaurant2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self):
        response = client.delete(
            reverse(self.get_delete_update, kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class EmployeeTest(TestCase):

    get_delete_update = 'get_delete_update_employee'
    get_post = 'get_post_employee'
    obj_serializer = EmployeeSerializer
    obj_class = Employee

    def setUp(self):
        self.employee1 = self.obj_class.objects.create(name="Employee1 full name 1", username="employee1")
        self.employee2 = self.obj_class.objects.create(name="Employee1 full name 2", username="employee2")
        self.employee3 = self.obj_class.objects.create(name="Employee1 full name 3", username="employee3")
        self.employee4 = self.obj_class.objects.create(name="Employee1 full name 4", username="employee4")

        self.valid_payload = {
            'name': 'Employee1 full name 5',
            'username': 'employee5',
        }
        self.valid_payload_put = {
            'name': 'Employee1 full name for PUT',
            'username': 'employee1_put',
        }
        self.invalid_payload = {
            'name': '',
            'username': '',
        }

    def test_get_all(self):
        response = client.get(reverse(self.get_post))
        objs = self.obj_class.objects.all()
        serializer = self.obj_serializer(objs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single(self):
        response = client.get(
            reverse(self.get_delete_update, kwargs={'pk': self.employee3.pk}))
        obj = self.obj_class.objects.get(pk=self.employee3.pk)
        serializer = self.obj_serializer(obj)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single(self):
        response = client.get(
            reverse(self.get_delete_update, kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid(self):
        response = client.post(
            reverse(self.get_post),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid(self):
        response = client.post(
            reverse(self.get_post),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update(self):
        response = client.put(
            reverse(self.get_delete_update, kwargs={'pk': self.employee1.pk}),
            data=json.dumps(self.valid_payload_put),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update(self):
        response = client.put(
            reverse(self.get_delete_update, kwargs={'pk': self.employee1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete(self):
        response = client.delete(
            reverse(self.get_delete_update, kwargs={'pk': self.employee2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self):
        response = client.delete(
            reverse(self.get_delete_update, kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class MenuTest(TestCase):

    get_delete_update = 'get_delete_update_menu'
    get_post = 'get_post_menu'
    obj_serializer = MenuSerializer
    obj_class = Menu

    def setUp(self):
        file = SimpleUploadedFile("pdf_for_text.pdf", b"file_content", content_type="text/pdf")
        fp = open(os.path.join(settings.MEDIA_ROOT + "/pdf_for_test.pdf"), 'rb')
        self.restaurant = Restaurant.objects.create(title='Restaurant 1')

        self.menu1 = self.obj_class.objects.create(title="Menu 1", restaurant=self.restaurant, filepath=file)
        self.menu2 = self.obj_class.objects.create(title="Menu 2", restaurant=self.restaurant, filepath=file)
        self.menu3 = self.obj_class.objects.create(title="Menu 3", restaurant=self.restaurant, filepath=file)
        self.menu4 = self.obj_class.objects.create(title="Menu 4", restaurant=self.restaurant, filepath=file)

        self.valid_payload = {
            'title': 'Menu 5',
            'restaurant': self.restaurant.id,
            'filepath': fp,
        }
        self.valid_payload_put = {
            'title': 'Menu for PUT',
            'restaurant': self.restaurant.id,
            'filepath': fp,
        }
        self.invalid_payload = {
            'title': '',
            'restaurant': '',
            'filepath': '',
        }

    def test_get_all(self):
        response = client.get(reverse(self.get_post))
        objs = self.obj_class.objects.all()
        serializer = self.obj_serializer(objs, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single(self):
        response = client.get(
            reverse(self.get_delete_update, kwargs={'pk': self.menu3.pk}))
        obj = self.obj_class.objects.get(pk=self.menu3.pk)
        serializer = self.obj_serializer(obj)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single(self):
        response = client.get(
            reverse(self.get_delete_update, kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid(self):
        response = client.post(
            reverse('create_edit_menu'),
            data=self.valid_payload,
            format='multipart',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid(self):
        response = client.post(
            reverse('create_edit_menu'),
            data=self.invalid_payload,
            format='multipart',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update(self):
        response = client.post(
            reverse('create_edit_menu', kwargs={'pk': self.menu1.pk}),
            data=self.valid_payload_put,
            format='multipart',
        )
        # sys.stderr.write(repr(response.data) + '\n')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update(self):
        response = client.post(
            reverse('create_edit_menu', kwargs={'pk': self.menu1.pk}),
            data=self.invalid_payload,
            format='multipart',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete(self):
        response = client.delete(
            reverse(self.get_delete_update, kwargs={'pk': self.menu2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self):
        response = client.delete(
            reverse(self.get_delete_update, kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_today(self):
        response = client.get(reverse('get_today_menu'))
        objs = self.obj_class.objects.filter(created_at=timezone.datetime.today())
        serializer = self.obj_serializer(objs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_menus_by_date(self):
        response = client.post(
            reverse('get_votes_by_date'),
            data=json.dumps({'day': 15, 'month': 3, 'year': 2019}),
            content_type='application/json'
        )
        objs = self.obj_class.objects.filter(created_at=datetime.date(2019, 3, 15))
        serializer = self.obj_serializer(objs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class VoteTest(TestCase):

    get_delete_update = 'get_delete_update_vote'
    get_post = 'get_post_vote'
    obj_serializer = VoteSerializer
    obj_class = Vote

    def setUp(self):
        file = SimpleUploadedFile("pdf_for_text.pdf", b"file_content", content_type="text/pdf")
        self.restaurant1 = Restaurant.objects.create(title='Restaurant 1')
        self.restaurant2 = Restaurant.objects.create(title='Restaurant 2')

        self.menu1 = Menu.objects.create(title="Menu 1", restaurant=self.restaurant1, filepath=file)
        self.menu2 = Menu.objects.create(title="Menu 2", restaurant=self.restaurant2, filepath=file)

        self.employee1 = Employee.objects.create(name="Employee 1 full name", username="employee1")
        self.employee2 = Employee.objects.create(name="Employee 2 full name", username="employee2")
        self.employee3 = Employee.objects.create(name="Employee 3 full name", username="employee3")

        self.vote1 = self.obj_class.objects.create(employee=self.employee1, menu=self.menu1)
        self.vote2 = self.obj_class.objects.create(employee=self.employee2, menu=self.menu2)

        self.valid_payload = {
            'employee': self.employee3.id,
            'menu': self.menu1.id,
        }
        self.valid_payload_put = {
            'employee': self.employee1.id,
            'menu': self.menu2.id,
        }
        self.invalid_payload = {
            'name': '',
            'username': '',
        }

    def test_get_all(self):
        response = client.get(reverse(self.get_post))
        objs = self.obj_class.objects.all()
        serializer = self.obj_serializer(objs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single(self):
        response = client.get(
            reverse(self.get_delete_update, kwargs={'pk': self.vote1.pk}))
        obj = self.obj_class.objects.get(pk=self.vote1.pk)
        serializer = self.obj_serializer(obj)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single(self):
        response = client.get(
            reverse(self.get_delete_update, kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid(self):
        response = client.post(
            reverse(self.get_post),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid(self):
        response = client.post(
            reverse(self.get_post),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update(self):
        response = client.put(
            reverse(self.get_delete_update, kwargs={'pk': self.vote1.pk}),
            data=json.dumps(self.valid_payload_put),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update(self):
        response = client.put(
            reverse(self.get_delete_update, kwargs={'pk': self.vote1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete(self):
        response = client.delete(
            reverse(self.get_delete_update, kwargs={'pk': self.vote2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self):
        response = client.delete(
            reverse(self.get_delete_update, kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_votes_by_date(self):
        response = client.post(
            reverse('get_votes_by_date'),
            data=json.dumps({'day': 15, 'month': 3, 'year': 2019}),
            content_type='application/json'
        )
        objs = self.obj_class.objects.filter(created_at=datetime.date(2019, 3, 15))
        serializer = self.obj_serializer(objs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

