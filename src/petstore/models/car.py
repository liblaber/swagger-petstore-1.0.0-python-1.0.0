from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"brand_name": "brandName", "model_name": "modelName"})
class Car(BaseModel):
    """Car

    :param brand_name:
    :type brand_name: str
    :param model_name:
    :type model_name: str
    :param year: , defaults to None
    :type year: int, optional
    """

    def __init__(self, brand_name: str, model_name: str, year: int = None):
        self.brand_name = brand_name
        self.model_name = model_name
        if year is not None:
            self.year = year
