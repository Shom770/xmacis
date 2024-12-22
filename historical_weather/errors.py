"""Defines the errors raised by this wrapper to convey to the user that their data/parameters are wrong."""


class IncorrectParametersError(Exception):
    """Raised when the parameters are passed in incorrectly."""
    def __init__(self, message):
        self.message = message

    def __str__(self) -> str:
        return f"The following parameters were passed in incorrectly: {self.message}"
