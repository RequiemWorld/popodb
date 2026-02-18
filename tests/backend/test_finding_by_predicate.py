import unittest
from popodb import DatabaseBackend
from . import FieldedTypeOne
from . import FieldedTypeTwo
from . import BackendTestFixture


class TestFindOneByPredicate(BackendTestFixture):

	def test_should_return_none_when_no_entities_in_backend(self):
		self.assertIsNone(self._backend.find_one_by_predicate(FieldedTypeOne, lambda entity: entity.field == "abc"))

	def test_should_return_entity_when_matching_one_is_in_backend(self):
		self._add_entity_to_backend(FieldedTypeOne(field="123"))
		matching_entity: FieldedTypeOne = self._backend.find_one_by_predicate(FieldedTypeOne, lambda entity: entity.field == "123")
		self.assertEqual("123", matching_entity.field)


class TestFindByPredicateMultipleTypes(BackendTestFixture):

	def test_should_return_none_when_there_is_entity_matching_predicate_but_not_with_given_type(self):
		entity = FieldedTypeTwo(field="111")
		self._add_entity_to_backend(entity)
		matching_entity = self._backend.find_one_by_predicate(FieldedTypeOne, lambda entity: entity.field == "111")
		self.assertIsNone(matching_entity)