from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.get_parameterless_ok_response import GetParameterlessOkResponse


class ValidationService(BaseService):

    @cast_models
    def get_primitives(
        self,
        min_max_integer: int,
        min_max_number: float,
        min_max_length_string: str,
        string_with_pattern: str,
        description_in_schema: str,
        description_in_parameter_and_schema: str,
    ) -> GetParameterlessOkResponse:
        """get_primitives

        :param min_max_integer: An integer with min -10 and max 10
        :type min_max_integer: int
        :param min_max_number: An number with min -1 and max 1
        :type min_max_number: float
        :param min_max_length_string: A string with minimum length of 2 and maximum length of 8
        :type min_max_length_string: str
        :param string_with_pattern: A string with a pattern (email format)
        :type string_with_pattern: str
        :param description_in_schema: description_in_schema
        :type description_in_schema: str
        :param description_in_parameter_and_schema: This description comes from the parameter
        :type description_in_parameter_and_schema: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(int).min(-10).max(10).validate(min_max_integer)
        Validator(float).min(-1).max(1).validate(min_max_number)
        Validator(str).min_length(2).max_length(8).validate(min_max_length_string)
        Validator(str).pattern("^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$").validate(
            string_with_pattern
        )
        Validator(str).validate(description_in_schema)
        Validator(str).validate(description_in_parameter_and_schema)

        serialized_request = (
            Serializer(
                f"{self.base_url}/validation/primitives", self.get_default_headers()
            )
            .add_query("minMaxInteger", min_max_integer)
            .add_query("minMaxNumber", min_max_number)
            .add_query("minMaxLengthString", min_max_length_string)
            .add_query("stringWithPattern", string_with_pattern)
            .add_query("descriptionInSchema", description_in_schema)
            .add_query(
                "descriptionInParameterAndSchema", description_in_parameter_and_schema
            )
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)
