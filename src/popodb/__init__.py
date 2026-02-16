

class FakeDatabase:

	def new_transaction(self) -> None:
		raise NotImplementedError
