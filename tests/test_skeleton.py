import unittest
from popodb import FakeDatabase


class TestFakeDatabaseSkeleton(unittest.TestCase):
	def setUp(self):
		self._fake_database = FakeDatabase()

	def test_should_raise_not_implemented_error_on_new_transaction(self):
		with self.assertRaises(NotImplementedError):
			self._fake_database.new_transaction()
