from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.person import Person
from ..models.get_parameterless_ok_response import GetParameterlessOkResponse
from ..models.car_or_person import CarOrPerson


class GeneralService(BaseService):

    @cast_models
    def get_parameterless(self) -> GetParameterlessOkResponse:
        """get_parameterless

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        serialized_request = (
            Serializer(
                f"{self.base_url}/general/parameterless", self.get_default_headers()
            )
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)

    @cast_models
    def get_only_primitives(
        self,
        int_param: int,
        string_param: str,
        number_param: float,
        bool_param: bool,
        deprecated_required_param: int,
        deprecated_optional_param: int = None,
    ) -> GetParameterlessOkResponse:
        """get_only_primitives

        :param int_param: int_param
        :type int_param: int
        :param string_param: string_param
        :type string_param: str
        :param number_param: number_param
        :type number_param: float
        :param bool_param: bool_param
        :type bool_param: bool
        :param deprecated_required_param: deprecated_required_param
        :type deprecated_required_param: int
        :param deprecated_optional_param: deprecated_optional_param, defaults to None
        :type deprecated_optional_param: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(int).validate(int_param)
        Validator(str).validate(string_param)
        Validator(float).validate(number_param)
        Validator(bool).validate(bool_param)
        Validator(int).validate(deprecated_required_param)
        Validator(int).is_optional().validate(deprecated_optional_param)

        serialized_request = (
            Serializer(
                f"{self.base_url}/general/only-primitives", self.get_default_headers()
            )
            .add_query("intParam", int_param)
            .add_query("stringParam", string_param)
            .add_query("numberParam", number_param)
            .add_query("boolParam", bool_param)
            .add_query("deprecatedRequiredParam", deprecated_required_param)
            .add_query("deprecatedOptionalParam", deprecated_optional_param)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)

    @cast_models
    def get_model_and_primitives(
        self, int_param: int, person_param: Person
    ) -> GetParameterlessOkResponse:
        """get_model_and_primitives

        :param int_param: int_param
        :type int_param: int
        :param person_param: person_param
        :type person_param: Person
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(int).validate(int_param)
        Validator(Person).validate(person_param)

        serialized_request = (
            Serializer(
                f"{self.base_url}/general/model-and-primitives",
                self.get_default_headers(),
            )
            .add_query("intParam", int_param)
            .add_query("personParam", person_param)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)

    @cast_models
    def post_model_and_primitives(
        self, request_body: Person, int_param: int
    ) -> GetParameterlessOkResponse:
        """post_model_and_primitives

        :param request_body: The request body.
        :type request_body: Person
        :param int_param: int_param
        :type int_param: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(Person).validate(request_body)
        Validator(int).validate(int_param)

        serialized_request = (
            Serializer(
                f"{self.base_url}/general/model-and-primitives",
                self.get_default_headers(),
            )
            .add_query("intParam", int_param)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)

    @cast_models
    def get_arrays_of_primitives(
        self,
        int_array_param: List[int],
        string_array_param: List[str],
        number_array_param: List[float],
        boolean_array_param: List[bool],
    ) -> GetParameterlessOkResponse:
        """get_arrays_of_primitives

        :param int_array_param: int_array_param
        :type int_array_param: List[int]
        :param string_array_param: string_array_param
        :type string_array_param: List[str]
        :param number_array_param: number_array_param
        :type number_array_param: List[float]
        :param boolean_array_param: boolean_array_param
        :type boolean_array_param: List[bool]
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(int).is_array().validate(int_array_param)
        Validator(str).is_array().validate(string_array_param)
        Validator(float).is_array().validate(number_array_param)
        Validator(bool).is_array().validate(boolean_array_param)

        serialized_request = (
            Serializer(
                f"{self.base_url}/general/arrays-of-primitives",
                self.get_default_headers(),
            )
            .add_query("intArrayParam", int_array_param)
            .add_query("stringArrayParam", string_array_param)
            .add_query("numberArrayParam", number_array_param)
            .add_query("booleanArrayParam", boolean_array_param)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)

    @cast_models
    def get_array_of_models(
        self, person_array: List[Person]
    ) -> GetParameterlessOkResponse:
        """get_array_of_models

        :param person_array: person_array
        :type person_array: List[Person]
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(Person).is_array().validate(person_array)

        serialized_request = (
            Serializer(
                f"{self.base_url}/general/array-of-models", self.get_default_headers()
            )
            .add_query("personArray", person_array)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)

    @cast_models
    def get_one_of(
        self, car_or_person_param: CarOrPerson
    ) -> GetParameterlessOkResponse:
        """get_one_of

        :param car_or_person_param: car_or_person_param
        :type car_or_person_param: CarOrPerson
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response with body
        :rtype: GetParameterlessOkResponse
        """

        Validator(CarOrPerson).validate(car_or_person_param)

        serialized_request = (
            Serializer(f"{self.base_url}/general/one-of", self.get_default_headers())
            .add_query("carOrPersonParam", car_or_person_param)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetParameterlessOkResponse._unmap(response)
