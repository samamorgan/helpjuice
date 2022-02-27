from pathlib import Path

from setuptools import find_packages
from setuptools import setup

root = Path(__file__).parent

with (root / "requirements.txt").open() as f:
    requires = f.read().splitlines()

about = {}
with (root / "helpjuice" / "__version__.py").open() as f:
    exec(f.read(), about)

with (root / "README.md").open() as f:
    readme = f.read()

setup(
    author_email=about["__author_email__"],
    author=about["__author__"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
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
        "Tracker": "https://github.com/samamorgan/helpjuice/issues",
        "Funding": "https://github.com/sponsors/samamorgan",
    },
    python_requires="~=3.6",
    url=about["__url__"],
    version=about["__version__"],
)
