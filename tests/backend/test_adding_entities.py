import unittest
from popodb import DatabaseBackend


class TestEntity:
	def __init__(self, name: str):
		self.name = name


class TestAddingEntitiesThroughMerge(unittest.TestCase):

	def test_should_add_single_entity_in_fresh_merge(self):
		entity = TestEntity(name="someone")
		backend = DatabaseBackend()
		backend.merge_entities([entity])
		matching_entity: TestEntity = backend.find_one_by_predicate(TestEntity, lambda entity: entity.name == "someone")
		self.assertEqual("someone", matching_entity.name)

	def test_should_add_multiple_entities_in_fresh_merge(self):
		entity_one = TestEntity(name="Name1")
		entity_two = TestEntity(name="Name2")
		backend = DatabaseBackend()
		backend.merge_entities([entity_one, entity_two])
		matching_entity_1: TestEntity = backend.find_one_by_predicate(TestEntity, lambda entity: entity.name == "Name1")
		matching_entity_2: TestEntity = backend.find_one_by_predicate(TestEntity, lambda entity: entity.name == "Name2")
		self.assertEqual("Name1", matching_entity_1.name)
		self.assertEqual("Name2", matching_entity_2.name)
