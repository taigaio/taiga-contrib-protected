import taiga_contrib_protected.storage


def test_backend_exists():
    backend_class = taiga_contrib_protected.storage.ProtectedFileSystemStorage
    backend = backend_class()
