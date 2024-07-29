from django.test import TestCase
from restaurant.views import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status


class MenuViewTest(TestCase):

    def setUp(self):
        # Initialize the APIClient
        self.client = APIClient()
        
        # Create test instances of the Menu model
        self.menu1 = Menu.objects.create(title="Pizza", price=10, inventory=20)
        self.menu2 = Menu.objects.create(title="Burger", price=8, inventory=50)
        self.menu3 = Menu.objects.create(title="Salad", price=6, inventory=10)

    def test_getall(self):
        # Send a GET request to the API endpoint that retrieves all Menu objects
        response = self.client.get('/restaurant/menu/')
        
        # Retrieve all Menu objects
        menus = Menu.objects.all()
        
        # Serialize the Menu objects
        serializer = MenuSerializer(menus, many=True)
        
        # Assert that the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert that the serialized data matches the response data
        self.assertEqual(response.data['results'], serializer.data)