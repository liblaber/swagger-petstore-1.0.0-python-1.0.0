"""
An enum class containing all the possible environments for the SDK
"""

from enum import Enum


class Environment(Enum):
    """The environments available for the SDK"""

    DEFAULT = "https://api.liblab.com"
    PRODUCTION = "https://api.liblab.com"
    STAGING = "https://api-staging.liblab.com"
    DEVELOPMENT = "https://api-dev.liblab.com"
