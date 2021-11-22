from django.test import TestCase
from dinners.models import Dinner
from users.models import User

# Create your tests here.
class DinnerTestCase(TestCase):
    def setUp(self):
        User.objects.create(username = "sig",
                            password = "passord",
                            email = "sig@ntnu.no",
                            first_name = "Sigurd",
                            last_name = "Hauan",
                            address = "Bergen"
                            )

        User.objects.create(username = "eiv",
                            password = "1234",
                            email = "eiv@ntnu.no",
                            first_name = "Eivind",
                            last_name = "Kjosbakken",
                            address = "Oslo"
                            )

        User.objects.create(username = "sig2",
                            password = "passord2",
                            email = "sig2@ntnu.no",
                            first_name = "Sigurd2",
                            last_name = "Hauan2",
                            address = "Bergen2"
                            )

        Dinner.objects.create(  title = "Pizza", 
                                description ="Pizza hos Sigurd",
                                place = "Bergen",
                                first_name = "Sigurd",
                                date = "10.02.2021",
                                time ="16.00",
                                max_guests = 4,
                                number_of_guests = 0,
                                guests = "",
                                allergies = "gluten",
                                category = "other",
                                host_username = "sig",
                                cost  = 100,
                                cost_per = 20
                                )

        Dinner.objects.create(  title = "Taco", 
                                description ="Taco hos Eivind",
                                place = "Oslo",
                                first_name = "Eivind",
                                date = "10.02.2021",
                                time ="16.00",
                                max_guests = 1,
                                number_of_guests = 0,
                                guests = "",
                                allergies = "egg",
                                category = "other",
                                host_username = "eiv",
                                cost = 50,
                                cost_per = 25
                                )
                                
    def testDinner(self):
        dinner = Dinner.objects.get(id = 1)
        self.assertEqual(dinner.title, "Pizza")
        self.assertEqual(dinner.description, "Pizza hos Sigurd")
        self.assertEqual(dinner.place, "Bergen")
        self.assertEqual(dinner.date, "10.02.2021")
        self.assertEqual(dinner.time, "16.00")
        self.assertEqual(dinner.max_guests, 4)
        self.assertEqual(dinner.number_of_guests, 0)
        dinner2 = Dinner.objects.get(id = 2)
        self.assertEqual(dinner2.title, "Taco")
        self.assertNotEqual(dinner.id, dinner2.id)
        dinner.add_or_remove_guest_to_guests("sig")
        dinner.add_or_remove_guest_to_guests("eiv")
        self.assertEqual(dinner.number_of_guests, 1) #Eier blir ikke lagt til
        self.assertEqual(dinner.guests, "eiv")
        dinner.add_guest_to_guests("eiv") #prøv å legg til eiv to ganger
        self.assertEqual(dinner.guests, "eiv")
        self.assertEqual(dinner.number_of_guests, 1)
        dinner.add_or_remove_guest_to_guests("eiv") # Fjerner Eiv fra guests
        self.assertEqual(dinner.guests, "")
        self.assertEqual(dinner.number_of_guests, 0)
        dinner2.add_or_remove_guest_to_guests("eiv")
        dinner2.add_or_remove_guest_to_guests("sig")
        dinner2.add_or_remove_guest_to_guests("sig2")
        self.assertEqual(dinner2.guests, "sig")
        self.assertEqual(dinner2.number_of_guests, dinner2.max_guests) 
        dinner.add_or_remove_guest_to_guests("eiv1")
        dinner.add_or_remove_guest_to_guests("eiv2")
        dinner.add_or_remove_guest_to_guests("eiv3")
        dinner.add_or_remove_guest_to_guests("eiv4")
        dinner.add_or_remove_guest_to_guests("eiv5")
        self.assertEqual(dinner.number_of_guests, dinner.max_guests)
        dinner.add_or_remove_guest_to_guests("eiv3")
        dinner.add_or_remove_guest_to_guests("eiv4")
        self.assertEqual(dinner.number_of_guests, 2)
        self.assertEqual(dinner.cost_per, 20)
        self.assertEqual(dinner2.cost_per, 25)
        
