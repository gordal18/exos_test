from django.test import TestCase
from datetime import datetime

from .models import User
from . import utils


class UtilsMethodTests(TestCase):
	def test_eligible_age1(self):
		test_date = datetime.strptime('Jun 27 2006', '%b %d %Y')
		self.assertIs(utils.is_eligible(test_date), False)

	def test_eligible_age2(self):
		test_date = datetime.strptime('Jun 27 1980', '%b %d %Y')
		self.assertIs(utils.is_eligible(test_date), True)

	def test_bizzfuzz1(self):
		self.assertEqual(utils.get_bizzfuzz(20), 'Fuzz')

	def test_bizzfuzz2(self):
		self.assertEqual(utils.get_bizzfuzz(12), 'Bizz')

	def test_bizzfuzz3(self):
		self.assertEqual(utils.get_bizzfuzz(30), 'BizzFuzz')

	def test_bizzfuzz4(self):
		self.assertEqual(utils.get_bizzfuzz(16), 16)
