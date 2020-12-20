from pathlib import Path

from setuptools import setup

packages = ["helpjuice"]

requires = ["requests"]

about = {}
with Path(__file__).parent.joinpath("helpjuice", "__version__.py").open() as f:
    exec(f.read(), about)

with open("README.md", "r") as f:
    readme = f.read()

setup(
    author_email=about["__author_email__"],
    author=about["__author__"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    description=about["__description__"],
    install_requires=requires,
    license=about["__license__"],
    long_description_content_type="text/markdown",
    long_description=readme,
    project_urls={
        "Documentation": about["__url__"],
        "Source": "https://github.com/samamorgan/helpjuice",
    },
    name=about["__title__"],
    packages=packages,
    url=about["__url__"],
    version=about["__version__"],
)
