from typing import Any
from typing import Callable

EntityType = object
FindEntityPredicate = Callable[[object], bool]


class DatabaseBackend:
	"""
	The backend piece of the in-memory fake database for POPOs.
	"""
	def __init__(self):
		self._entities: dict[EntityType, list[EntityType]] = dict()

	def merge_entities(self, entities: list[object]) -> None:
		for entity in entities:
			entity_type = type(entity)
			entities_list = self._entities.get(entity_type)
			if entities_list is None:
				entities_list = []
				self._entities[entity_type] = entities_list
			entities_list.append(entity)

	def find_one_by_predicate(self, type_: EntityType, predicate: FindEntityPredicate) -> Any | None:
		entities_list = self._entities.get(type_, [])
		for entity in entities_list:
			if predicate(entity):
				return entity
		return None


class FakeDatabase:

	def new_transaction(self) -> None:
		raise NotImplementedError
