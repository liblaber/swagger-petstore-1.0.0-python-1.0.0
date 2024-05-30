from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.person import Person
from ..models.get_parameterless_ok_response import GetParameterlessOkResponse


class RequestInputService(BaseService):

    @cast_models
    def post_strings(self, request_body: str) -> GetParameterlessOkResponse:
        """post_strings

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/request-input/strings", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)

    @cast_models
    def post_integer(self, request_body: int) -> GetParameterlessOkResponse:
        """post_integer

        :param request_body: The request body.
        :type request_body: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(int).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/request-input/integer", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)

    @cast_models
    def post_boolean(self, request_body: bool) -> GetParameterlessOkResponse:
        """post_boolean

        :param request_body: The request body.
        :type request_body: bool
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(bool).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/request-input/boolean", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)

    @cast_models
    def post_array_of_primitives(
        self, request_body: List[str]
    ) -> GetParameterlessOkResponse:
        """post_array_of_primitives

        :param request_body: The request body.
        :type request_body: List[str]
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(str).is_array().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/request-input/array", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)

    @cast_models
    def post_array_of_objects(
        self, request_body: List[Person]
    ) -> GetParameterlessOkResponse:
        """post_array_of_objects

        :param request_body: The request body.
        :type request_body: List[Person]
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(Person).is_array().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/request-input/array", self.get_default_headers()
            )
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)
