from django.test import TestCase
from rest_framework import status
# from unittest import TestCase
class GetTest(TestCase):
    
    def test_home_test(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
# Create your tests here.
