from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from users.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username = "Håkon",
                            password="123",
                            age = 12,
                            address = "skomakergata",
                            allergies = "gluten")

        User.objects.create(username="Håkon2",
                            password="123",
                            age=16,
                            address="Skomakergata",
                            allergies="Laktose")

    def testDinner(self):
        user = User.objects.get(id=1)
        user2 = User.objects.get(id=2)
        self.assertEqual(user.age, 12)
        self.assertEqual(user.address, "skomakergata")
        self.assertEqual(user.allergies, "gluten")
        self.assertEqual(user.is_admin, False)

        self.assertEqual(user2.age, 16)
        self.assertEqual(user2.allergies, "Laktose")

        self.assertEqual(user.password, user2.password)

        self.assertNotEqual(user2.address, "Blåfjellveien")

