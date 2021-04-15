# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos Ventures SL

from unittest import mock


class FileSystemStorageStub:
    def url(self, path):
        return "http://protected.server.test/" + str(path)


# Mock imported modules
import sys

sys.modules["django.conf"] = mock.Mock(settings=mock.Mock(SECRET_KEY="taiga-secret-key"))
sys.modules["taiga.base.storage"] = mock.Mock(FileSystemStorage=FileSystemStorageStub)

import taiga_contrib_protected.storage


def test_backend_exists():
    backend_class = taiga_contrib_protected.storage.ProtectedFileSystemStorage
    backend = backend_class()
    url = backend.url("path/to/file.ext")
    assert url.startswith("http")
    assert "?token=" in url
