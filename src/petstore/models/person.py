from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .address import Address


@JsonMap(
    {
        "first_name": "firstName",
        "last_name": "lastName",
        "accepted_terms": "acceptedTerms",
        "required_deprecated": "requiredDeprecated",
        "optional_deprecated": "optionalDeprecated",
    }
)
class Person(BaseModel):
    """Person

    :param first_name:
    :type first_name: str
    :param last_name:
    :type last_name: str
    :param accepted_terms:
    :type accepted_terms: bool
    :param age: , defaults to None
    :type age: int, optional
    :param address:
    :type address: Address
    :param required_deprecated:
    :type required_deprecated: int
    :param optional_deprecated: , defaults to None
    :type optional_deprecated: str, optional
    """

    def __init__(
        self,
        first_name: str,
        last_name: str,
        accepted_terms: bool,
        address: Address,
        required_deprecated: int,
        age: int = None,
        optional_deprecated: str = None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.accepted_terms = accepted_terms
        if age is not None:
            self.age = age
        self.address = self._define_object(address, Address)
        self.required_deprecated = required_deprecated
        if optional_deprecated is not None:
            self.optional_deprecated = optional_deprecated
