""" Custom Exceptions """
from pytube.exceptions import PytubeError


class InvalidUrl(Exception):
    """Excdeption Class for Invalid URL"""

    pass


class DownloadError(PytubeError):
    """Exception for Download Failure"""

    pass
