from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(username='cfe', email='hi@gmail.com')
        user.set_password('123')
        user.save()
        return 
    
    def test_create_user(self):
        qs = User.objects.filter(username='cfe')
        self.assertEqual(qs.count(), 1)