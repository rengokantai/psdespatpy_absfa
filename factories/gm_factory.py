from .abs_factory import AbsFactory
from autos.gm.spark import ChevySpark
from autos.gm.camaro import ChevyCamaro

class GMFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return ChevySpark()

    @staticmethod
    def create_sport():
        return ChevyCamaro()