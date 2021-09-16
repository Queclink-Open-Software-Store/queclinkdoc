#!/usr/bin/env python
# Thanks Alabaster (https://github.com/bitprophet/alabaster) very much.

import codecs
from setuptools import setup

_locals = {}
with open("queclinkdoc/_version.py") as fp:
    exec(fp.read(), None, _locals)
version = _locals["__version__"]

with codecs.open("README.rst", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="queclinkdoc",
    version=version,
    description="A simple, clean, friendly, and less-configured Sphinx theme",
    long_description=readme,
    author="Queclink Wireless Solutions Co., Ltd.",
    author_email="Hubert.Lee@queclink.com",
    url="https://github.com/Queclink-Open-Software-Store/queclinkdoc",
    packages=["queclinkdoc"],
    include_package_data=True,
    entry_points={"sphinx.html_themes": ["queclinkdoc = queclinkdoc"]},
)
