from django.test import TestCase
from django.core.exceptions import ValidationError


from cities.models import City
from trains.models import Train

class RouteTestCase(TestCase):
    
    def setUp(self):
        self.city_A = City.objects.create(name='A')
        self.city_B = City.objects.create(name='B')
        self.city_C = City.objects.create(name='C')
        self.city_D = City.objects.create(name='D')
        self.city_E = City.objects.create(name='E')
        t1 = Train(name='t1', from_city=self.city_A, to_city=self.city_B, travel_time=9)
        t1.save()
        t2 = Train(name='t2', from_city=self.city_B, to_city=self.city_D, travel_time=8)
        t2.save()
        t3 = Train(name='t3', from_city=self.city_A, to_city=self.city_C, travel_time=7)
        t3.save()
        t4 = Train(name='t4', from_city=self.city_C, to_city=self.city_B, travel_time=6)
        t4.save()
        t5 = Train(name='t5', from_city=self.city_B, to_city=self.city_E, travel_time=3)
        t5.save()
        t6 = Train(name='t6', from_city=self.city_B, to_city=self.city_A, travel_time=11)
        t6.save()
        t7 = Train(name='t7', from_city=self.city_A, to_city=self.city_C, travel_time=10)
        t7.save()
        t8 = Train(name='t8', from_city=self.city_E, to_city=self.city_D, travel_time=5)
        t8.save()
        t9 = Train(name='t9', from_city=self.city_D, to_city=self.city_E, travel_time=4)
        t9.save()

    def test_model_city_duplicate(self):
        try:
            a_city = City(name='A')
            a_city.full_clean()
        except ValidationError as e:
            self.assertEqual({'name': ['Город with this Город already exists.']}, e.message_dict)

    def test_model_train_duplicate(self):
        try:
            train = Train(name='t2', from_city=self.city_B, to_city=self.city_D, travel_time=4)
            train.full_clean()
        except ValidationError as e:
            self.assertEqual({'name': ['Поезд with this Номер поезда already exists.']}, e.message_dict)   
        try:
            train = Train(name='t12', from_city=self.city_B, to_city=self.city_D, travel_time=8)
            train.full_clean()
        except ValidationError as e:
            self.assertEqual({'__all__': ['Измените время в пути']}, e.message_dict)    