import urllib.parse

from django.conf import settings

from ._vendor.itsdangerous import TimestampSigner

from taiga.base.storage import FileSystemStorage


class ProtectedFileSystemStorage(FileSystemStorage):
    def url(self, name):
        orig = super().url(name)
        signer = TimestampSigner(settings.SECRET_KEY, sep=":", salt="taiga-protected")
        signature = signer.sign(name)
        signature = signature.decode("utf-8")
        _, _, token = signature.partition(":")
        qs = urllib.parse.urlencode({"token": token})
        return "%s?%s" % (orig, qs)
