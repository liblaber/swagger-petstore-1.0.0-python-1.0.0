from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .node import Node
from .address import Address


@JsonMap(
    {
        "leaf_node": "leafNode",
        "home_address": "homeAddress",
        "work_address": "workAddress",
    }
)
class CircularReferenceTestModel(BaseModel):
    """A model for testing circular references in snippet. It has 2 'Address'es to ensure that the solution won't fail to build two of the same model unless it's an actual circular reference.

    :param leaf_node: , defaults to None
    :type leaf_node: Node, optional
    :param home_address: , defaults to None
    :type home_address: Address, optional
    :param work_address: , defaults to None
    :type work_address: Address, optional
    """

    def __init__(
        self,
        leaf_node: Node = None,
        home_address: Address = None,
        work_address: Address = None,
    ):
        if leaf_node is not None:
            self.leaf_node = self._define_object(leaf_node, Node)
        if home_address is not None:
            self.home_address = self._define_object(home_address, Address)
        if work_address is not None:
            self.work_address = self._define_object(work_address, Address)
