from django.test import TestCase
from ..models import *
from django.core.files.uploadedfile import SimpleUploadedFile


class RestaurantTest(TestCase):

    def setUp(self):
        Restaurant.objects.create(title="Restaurant1")

    def test_instance(self):
        obj = Restaurant.objects.get(id=1)
        self.assertEqual(
            obj.title, "Restaurant1")


class EmployeeTest(TestCase):

    def setUp(self):
        Employee.objects.create(username='Employee1', name='Employee1 full name')

    def test_instance(self):
        obj = Employee.objects.get(username="Employee1")
        self.assertEqual(
            obj.username, "Employee1")
        self.assertEqual(
            obj.name, "Employee1 full name")


class MenuTest(TestCase):

    def setUp(self):
        file = SimpleUploadedFile("pdf_for_text.pdf", b"file_content", content_type="text/pdf")
        Restaurant.objects.create(title="Restaurant1")
        restaurant = Restaurant.objects.get(id=1)
        Menu.objects.create(restaurant_id=restaurant.id, filepath=file)

    def test_instance(self):
        obj = Menu.objects.get(id=1)
        self.assertEqual(
            obj.restaurant_id, 1)


class VoteTest(TestCase):

    def setUp(self):
        file = SimpleUploadedFile("pdf_for_text.pdf", b"file_content", content_type="text/pdf")
        Restaurant.objects.create(title='Restaurant1')
        Employee.objects.create(username='Employee1', name='Employee1 full name')
        restaurant = Restaurant.objects.get(id=1)
        employee = Employee.objects.get(id=1)
        Menu.objects.create(restaurant_id=restaurant.id, filepath=file)

        menu = Menu.objects.get(id=1)
        Vote.objects.create(employee_id=employee.id, menu_id=menu.id)

    def test_instance(self):
        obj = Vote.objects.get(id=1)
        self.assertEqual(obj.employee_id, 1)
        self.assertEqual(obj.menu_id, 1)

