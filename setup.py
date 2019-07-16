from setuptools import setup, find_packages

setup(
    name="pymods",
    version="0.3.0",
    packages=find_packages(),
    install_requires=['lxml >= 4.3.4'],
    author="Matt Cordial",
    author_email="matt.cordial@gmail.com",
    description=(
        "Utility class wrapping lxml for building MODS v3.4 XML metadata."
    ),
    keywords="MODS metadata xml",
)
