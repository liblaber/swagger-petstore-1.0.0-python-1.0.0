from .services.general import GeneralService
from .services.validation import ValidationService
from .services.request_input import RequestInputService
from .services.misc import MiscService
from .net.environment import Environment


class Petstore:
    def __init__(
        self, access_token: str = None, base_url: str = Environment.DEFAULT.value
    ):
        """
        Initializes Petstore the SDK class.
        """
        self.general = GeneralService(base_url=base_url)
        self.validation = ValidationService(base_url=base_url)
        self.request_input = RequestInputService(base_url=base_url)
        self.misc = MiscService(base_url=base_url)
        self.set_access_token(access_token)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.general.set_base_url(base_url)
        self.validation.set_base_url(base_url)
        self.request_input.set_base_url(base_url)
        self.misc.set_base_url(base_url)

        return self

    def set_access_token(self, access_token: str):
        """
        Sets the access token for the entire SDK.
        """
        self.general.set_access_token(access_token)
        self.validation.set_access_token(access_token)
        self.request_input.set_access_token(access_token)
        self.misc.set_access_token(access_token)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
