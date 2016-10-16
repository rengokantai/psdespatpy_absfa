from .abs_factory import AbsFactory
from autos.ford.fiesta import FordFiesta
from autos.ford.mustang import FordMustang
class FordFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()

    @staticmethod
    def create_sport():
        return FordMustang()