=======================
taiga-contrib-protected
=======================

This package implements an alternative storage system for taiga.

This is a part of the system. To run it also needs:

- nginx with specific configuration

- and taiga-protected service as the backend to validate requests.


.. code::

    #########################################
    ## Media Static settings
    #########################################

    MEDIA_URL = "https://media-domain.example.com/"
    MEDIA_ROOT = "/path/to/media"
    DEFAULT_FILE_STORAGE = "taiga_contrib_protected.storage.ProtectedFileSystemStorage"
    THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE


Vendoring
=========

How to update vendored libraries.

.. code::

   pip install -t taiga_contrib_protected/_vendor -r taiga_contrib_protected/_vendor/vendor.txt --no-compile --no-deps
   rm -rf taiga_contrib_protected/_vendor/*.dist-info
