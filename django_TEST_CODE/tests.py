from django.test import TestCase

# Create your tests here.
from . models import Flight,Airport

class TestFightCase(TestCase):
   def setUp(self):
        a1 = Airport.objects.create(code='AAA',city="city A")
        a2 = Airport.objects.create(code="BBB", city="city B")

        Flight.objects.create(origin=a1,destination=a2,duration=100)
        Flight.objects.create(origin=a1,destination=a1,duration=100)
        Flight.objects.create(origin=a1,destination=a1,duration=-111)
        
        def test_departure_count(self):
            a = Airport.objects.get(code="AAA")
            self.assertEqual(a.depa.count(),3)
        
        def test_arrival_count(self):
            a = Airport.objects.get(code="AAA")
            self.assertEqual(a.arival.count(),1)

        def valid_flight(self):
            a1 = Airport.objects.get(code="AAA")
            a2 = Airport.objects.get(code="BBB")
            flight = Flight.objects.get(origin=a1,destination=a2,duration=100)
            self.assertTrue(flight.is_valid_flight())
