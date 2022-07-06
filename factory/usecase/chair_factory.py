"""The Factory Class"""
from factory.usecase.small_chair import SmallChair
from factory.usecase.medium_chair import MediumChair
from factory.usecase.big_chair import BigChair


class ChairFactory:  # pylint: disable=too-few-public-methods
    """The Factory Class"""

    @staticmethod
    def get_chair(chair):
        """A static method to get a chair"""
        if chair == 'BigChair':
            return BigChair()
        if chair == 'MediumChair':
            return MediumChair()
        if chair == 'SmallChair':
            return SmallChair()
        else:
            raise NotImplementedError
