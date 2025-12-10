class OwletError(Exception):
    """Generic exception."""


class OwletConnectionError(OwletError):
    """When a connection error occurs."""


class OwletAuthenticationError(OwletError):
    """When login details are incorrect."""


class OwletCredentialsError(OwletError):
    """When login creds are incorrect, api no longer returns if this is username or password that is incorrect."""


class OwletDevicesError(OwletError):
    """when no devices are found."""


class OwletEmailError(OwletCredentialsError):
    """When the provided email is invalid or unknown."""


class OwletPasswordError(OwletCredentialsError):
    """When the provided password is invalid."""
