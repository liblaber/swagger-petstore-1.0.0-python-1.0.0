from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class GetParameterlessOkResponse(BaseModel):
    """GetParameterlessOkResponse

    :param status: , defaults to None
    :type status: str, optional
    """

    def __init__(self, status: str = None):
        if status is not None:
            self.status = status
