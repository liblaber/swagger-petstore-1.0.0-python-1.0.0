from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.get_parameterless_ok_response import GetParameterlessOkResponse
from ..models.circular_reference_test_model import CircularReferenceTestModel


class MiscService(BaseService):

    @cast_models
    def get_parameterless_with_no_response(self):
        """get_parameterless_with_no_response

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        serialized_request = (
            Serializer(
                f"{self.base_url}/misc/no-response-body", self.get_default_headers()
            )
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def get_optional_parameters(
        self,
        optional_int_param: int = None,
        optional_string_param: str = None,
        optional_number_param: float = None,
        optional_bool_param: bool = None,
    ) -> GetParameterlessOkResponse:
        """get_optional_parameters

        :param optional_int_param: optional_int_param, defaults to None
        :type optional_int_param: int, optional
        :param optional_string_param: optional_string_param, defaults to None
        :type optional_string_param: str, optional
        :param optional_number_param: optional_number_param, defaults to None
        :type optional_number_param: float, optional
        :param optional_bool_param: optional_bool_param, defaults to None
        :type optional_bool_param: bool, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(int).is_optional().validate(optional_int_param)
        Validator(str).is_optional().validate(optional_string_param)
        Validator(float).is_optional().validate(optional_number_param)
        Validator(bool).is_optional().validate(optional_bool_param)

        serialized_request = (
            Serializer(
                f"{self.base_url}/misc/optional-parameters", self.get_default_headers()
            )
            .add_query("optionalIntParam", optional_int_param)
            .add_query("optionalStringParam", optional_string_param)
            .add_query("optionalNumberParam", optional_number_param)
            .add_query("optionalBoolParam", optional_bool_param)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)

    @cast_models
    def deprecated_operation(self) -> GetParameterlessOkResponse:
        """deprecated_operation

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        serialized_request = (
            Serializer(
                f"{self.base_url}/misc/optional-parameters", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)

    @cast_models
    def post_circular_reference(
        self, request_body: CircularReferenceTestModel
    ) -> GetParameterlessOkResponse:
        """post_circular_reference

        :param request_body: The request body.
        :type request_body: CircularReferenceTestModel
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(CircularReferenceTestModel).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/misc/circular-reference", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)
