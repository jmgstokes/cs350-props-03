# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import Client
from django.test import reverse
from django.test import urlencode

# Create your tests here.

class TestPropertyViews(TestCase):

	def test_lookup_distance_view(self):
		client = Client()
		query_str1 = urlencode({'location':'1009 Diamond St, Las Vegas, NM'})
		query_str2 = urlencode({'distance':'100'})
		url = reverse('distance') + '?' + query_str1 + query_str2
		response = client.get(url)
		result_var = response.context['result']



		self.assertEqual(result_var.length = 2, True)

	def test_number_of_results(self):
		client = Client()
		query_str = urlencode({'query':'Condo'})
		url = reverse('query') + '?' + query_str
		response = client.get(url)
		result_var = response.context['result']


		self.assertEqual(result_var.length > 1, True)