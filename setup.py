"""Package Release"""

from __future__ import annotations

from setuptools import find_packages, setup

setup(
    name="pytube-downloader",
    version="1.0.0",
    description="Wrapper over pytube python's package",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Shubham Raj",
    author_email="shubhamraj2202@gmail.com",
    url="https://github.com/shubhamraj2202/pytube-downloader",
    packages=find_packages(include=["src", "src.*"]),
    install_requires=[],
    tests_require=["pytest"],
    project_urls={
        "Bug Reports": "https://github.com/shubhamraj2202/pytube-downloader/issues",
    },
)
