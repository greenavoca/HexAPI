from . models import Image, UserProfile
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class ImageTestCase(APITestCase):
    """
    Test suite for Image
    """

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/images/'
        self.user_a = User.objects.create_user(username='test_user', email='test@django.com', password='test1234')
        self.user_a.is_staff = True
        self.user_a.is_superuser = True
        self.profile_object = UserProfile.objects.create(user=self.user_a)

    def test_auth_required(self):
        """
        test if access is not permitted when unauthenticated
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_image(self):
        """
        test if logged user can upload a file
        """
        self.client.login(username='test_user', password='test1234')
        with open('media/test/test.jpg', 'rb') as image:
            data = {
                'image': image
            }
            response = self.client.post(self.url, data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_image_is_jpg_png(self):
        """
        test if uploaded image has proper extension -> png/jpg
        """
        self.client.login(username='test_user', password='test1234')
        with open('media/test/test1.gif', 'rb') as image:
            data = {
                'image': image
            }
            response = self.client.post(self.url, data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



