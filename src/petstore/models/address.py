from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class State(Enum):
    """An enumeration representing different categories.

    :cvar CA: "CA"
    :vartype CA: str
    :cvar NY: "NY"
    :vartype NY: str
    :cvar TX: "TX"
    :vartype TX: str
    :cvar FL: "FL"
    :vartype FL: str
    """

    CA = "CA"
    NY = "NY"
    TX = "TX"
    FL = "FL"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, State._member_map_.values()))


@JsonMap({})
class Address(BaseModel):
    """Address

    :param street: , defaults to None
    :type street: str, optional
    :param city:
    :type city: str
    :param number: , defaults to None
    :type number: str, optional
    :param state:
    :type state: State
    """

    def __init__(self, city: str, state: State, street: str = None, number: str = None):
        if street is not None:
            self.street = street
        self.city = city
        if number is not None:
            self.number = number
        self.state = self._enum_matching(state, State.list(), "state")
