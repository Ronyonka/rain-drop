from django.test import TestCase
from datetime import date
from .models import *
from .forms import *


class RainModelTest(TestCase):
    def setUp(self):
        self.rain = Rain.objects.create(date='2019-05-07', amount =900)

    def testInstance(self):
        self.assertTrue(isinstance(self.rain, Rain))
        self.assertEqual(Rain.objects.count(), 1)


    def test_form_data(self):
        form_data = {'date':'2019-03-07', 'amount': 900}
        form = RainForm(data=form_data)
        self.assertTrue(form.is_valid)
        form.save()
        self.assertEqual(Rain.objects.count(), 2)

    def test_cannot_post_future_date(self):
        form_data = {'date':'2020-03-07', 'amount': 900}
        form = RainForm(data=form_data)
        self.assertTrue(form.is_valid)
        form.save()
        self.assertEqual(Rain.objects.count(), 2)

    def test_cannot_post_duplicate_data(self):
        form_data = {'date':'2019-03-07', 'amount': 900}
        form = RainForm(data=form_data)
        self.assertTrue(form.is_valid)
        form.save()
        self.assertEqual(Rain.objects.count(), 2)

    def tearDown(self):
        self.rain.delete()