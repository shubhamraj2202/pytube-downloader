"""
Python Youtube Downloader App
"""

from __future__ import annotations

import os
import ssl
from tkinter.messagebox import NO
from typing import Any, Optional
from urllib.error import URLError

from pytube import Caption, Stream, YouTube

from ytube.custom_exeptions import DownloadError
from ytube.model import Url


class PyYTD:
    """Python Youtube Downloader"""

    def __init__(
        self,
        link: str,
        resolution: Optional[str] = "",
        **kwargs: Optional[Any],
    ) -> None:
        """
        Initiaze Class Attributes
        Args:
            link (str): Link of Video
            resolution (str, optional): Video resolution i.e. "720p",
                       "480p", "360p", "240p", "144p". Defaults to None.
        """
        self.url: Url = Url(link=link)
        self.resolution: str = resolution
        self.caption_codes: str = kwargs.get("caption_codes", "en")
        self.youtube: YouTube = YouTube(self.url.link)
        self.download_path: os.PathLike = kwargs.get("download_path", ".")
        self.__post__()

    def __str__(self) -> str:
        return f"<{self.youtube.title}>"

    def __post__(self) -> None:
        """Post Init Method"""
        try:
            _ = str(self)
        except URLError:
            ssl._create_default_https_context = ssl._create_stdlib_context

    def get_captions(self, text: bool = True) -> Caption | str:
        """Fetch Video Captions"""
        caption: Caption | str = ""
        if self.youtube.captions:
            caption = self.youtube.captions.get_by_language_code(self.caption_codes)
        if caption and text:
            return caption.generate_srt_captions()
        return caption

    def download(self, download_path: os.PathLike | str = ".") -> os.PathLike | str:
        """
        Download Video at given or current path
        Returns:
            os.PathLike | str: Path of downloaded video
        """
        downloaded_path: os.PathLike | str = ""
        stream: Stream = self.youtube.streams.get_highest_resolution()
        if self.resolution:
            stream: Stream = self.youtube.streams.get_by_resolution(self.resolution)
        try:
            downloaded_path = stream.download(output_path=download_path)
        except DownloadError:
            print("An error has occurred while downloading")
        return downloaded_path
