from pathlib import Path

from setuptools import find_packages
from setuptools import setup

path = Path(__file__).parent

with path.joinpath("requirements.txt").open() as f:
    requires = f.read().splitlines()

about = {}
with path.joinpath("helpjuice", "__version__.py").open() as f:
    exec(f.read(), about)

with open("README.md", "r") as f:
    readme = f.read()

setup(
    author_email=about["__author_email__"],
    author=about["__author__"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description=about["__description__"],
    install_requires=requires,
    license=about["__license__"],
    long_description_content_type="text/markdown",
    long_description=readme,
    name=about["__title__"],
    packages=find_packages(),
    project_urls={
        "Documentation": about["__url__"],
        "Source": "https://github.com/samamorgan/helpjuice",
    },
    python_requires="~=3.6",
    url=about["__url__"],
    version=about["__version__"],
)
