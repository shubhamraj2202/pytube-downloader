""" Test PyYTD"""
import os
from typing import List

from pyhelper.misc import _map, get_files

from ytube.downloader import PyYTD
from ytube.model import Url, ValidationError


class TestYtube:
    """Test PyYTD"""

    def setup_method(self):
        """Setup Test Args"""
        link = "https://www.youtube.com/watch?v=lG6ZCswlkm8"
        self.pytd = PyYTD(link)

    def teardown_method(self):
        """Clean Up"""
        mp4_files: List[os.PathLike] = get_files(path=os.getcwd(), suffix=".mp4")
        _map(lambda file: os.remove(file), mp4_files)

    def test_url(self):
        """Test if URL is Valid"""
        assert isinstance(self.pytd.url, Url)

    def test_invalid_url(self):
        """Test if URL is Invalid"""
        link = "www.youtube.com/watch?v=lG6ZCswlkm8"
        error = None
        try:
            _ = Url(link=link, raise_errors=True)
        except Exception as err:
            error = err
        assert isinstance(error, ValidationError)

    def test_download(self):
        """Test Down Success"""
        path = self.pytd.download()
        assert path.endswith(".mp4")

    def test_captions(self):
        """Test Video Captios"""
        assert not self.pytd.get_captions()
