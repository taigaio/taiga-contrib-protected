#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos Ventures SL

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
    license = 'MPL-2',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
