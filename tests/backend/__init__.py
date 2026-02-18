import unittest
from popodb import DatabaseBackend



class FieldedTypeOne:
	def __init__(self, field: str):
		self.field = field


class FieldedTypeTwo:
	def __init__(self, field: str):
		self.field = field


class BackendTestFixture(unittest.TestCase):
	def setUp(self):
		self._backend = DatabaseBackend()

	def _add_entity_to_backend(self, entity: object) -> None:
		self._backend.merge_entities([entity])

