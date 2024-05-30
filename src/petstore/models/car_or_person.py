from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .car import Car
from .person import Person


class CarOrPersonGuard(OneOfBaseModel):
    class_list = {"Car": Car, "Person": Person}


CarOrPerson = Union[Car, Person]
