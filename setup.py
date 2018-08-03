#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="taiga-contrib-protected",
    version="18.8.0.dev0",
    description="The Taiga plugin for protected attachments",
    long_description="",
    keywords="taiga, download, protected",
    author="Miguel González",
    author_email="migonzalvar@gmail.com",
    url="https://github.com/migonzalvar/taiga-contrib-protected",
    license="AGPL",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
