import abc

class AbsFactory(metaclass=abc.ABCMeta):
	@abc.abstractstaticmethod
	def create_economy():
		pass
	
	@abc.abstractstaticmethod
	def create_sport():
		pass