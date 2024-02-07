.. _install:

Installation
============

.. meta::
    :description: How to install insertokname-authlib with pip, source code, etc.

This part of the documentation covers the installation of insertokname-authlib, just
like any other software package needs to be installed first.


$ pip install insertokname-authlib
---------------------


Installing insertokname-authlib is simple with `pip <http://www.pip-installer.org/>`_::

    $ pip install insertokname-authlib

It will also install the dependencies:

- cryptography

.. note::
    You may enter problems when installing cryptography, check its official
    document at https://cryptography.io/en/latest/installation/

Using insertokname-authlib with requests::

    $ pip install insertokname-authlib requests

Using insertokname-authlib with httpx::

    $ pip install insertokname-authlib httpx

Using insertokname-authlib with Flask::

    $ pip install insertokname-authlib Flask

Using insertokname-authlib with Django::

    $ pip install insertokname-authlib Django

Using insertokname-authlib with Starlette::

    $ pip install insertokname-authlib httpx Starlette

.. versionchanged:: v0.12

    "requests" is an optional dependency since v0.12. If you want to use
    insertokname-authlib client, you have to install "requests" by yourself::

    $ pip install insertokname-authlib requests

Get the Source Code
-------------------

insertokname-authlib is actively developed on GitHub, where the code is
`always available <https://github.com/lepture/insertokname-authlib>`_.

You can either clone the public repository::

    $ git clone git://github.com/lepture/insertokname-authlib.git

Download the `tarball <https://github.com/lepture/insertokname-authlib/tarball/master>`_::

    $ curl -OL https://github.com/lepture/insertokname-authlib/tarball/master

Or, download the `zipball <https://github.com/lepture/insertokname-authlib/zipball/master>`_::

    $ curl -OL https://github.com/lepture/insertokname-authlib/zipball/master


Once you have a copy of the source, you can embed it in your Python package,
or install it into your site-packages easily::

    $ cd insertokname-authlib
    $ pip install .
