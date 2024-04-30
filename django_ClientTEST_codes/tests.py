from django.test import TestCase, Client
from django.db.models import Max
# Create your tests here.
from . models import Flight,Airport,Passanger

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

    def test_index(self):
        c = Client()
        res = c.get("/flights/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context["flights"].count(),3)

    def test_valid_flight_page(self):
        a1 = Airport.objects.get(code="AAA")
        f = Flight.objects.get(origin=a1,destination=a1)
        c = Client()
        res  = c.get(f"/flights/{f.id}")
        self.assertEqual(res.status_code, 200)
    def test_invalid_flight_page(self):
        maxid = Flight.objects.all().aggregate(Max("id"))["id_max"]
        c = Client()
        res = c.get(f"/flights/{maxid+1}")
        self.assertEqual(res.status_code, 404)

    def testFlightPagePassanger(self):
        f = Flight.objects.get(pk=1)
        p = Passanger.objects.create(first="Alix",last="ernst")
        f.passanger.add(p)
        
        c = Client()
        res = c.get(f"/flights/{f.id}")
        self.assertEqual(res.status_code,200)
        self.assertEqual(res.context['passanger'].count(),1)
        