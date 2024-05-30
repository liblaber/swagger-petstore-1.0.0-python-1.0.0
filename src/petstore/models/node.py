from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"other_children": "otherChildren"})
class Node(BaseModel):
    """Node

    :param name:
    :type name: str
    :param next: , defaults to None
    :type next: Node, optional
    :param previous: , defaults to None
    :type previous: Node, optional
    :param other_children: To test if it works with an array in-between, defaults to None
    :type other_children: List[Node], optional
    """

    def __init__(
        self,
        name: str,
        next: Node = None,
        previous: Node = None,
        other_children: List[Node] = None,
    ):
        self.name = name
        if next is not None:
            self.next = self._define_object(next, Node)
        if previous is not None:
            self.previous = self._define_object(previous, Node)
        if other_children is not None:
            self.other_children = self._define_list(other_children, Node)
