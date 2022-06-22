# helpjuice

## A Python wrapper of the Helpjuice API

[![Version](https://img.shields.io/pypi/v/helpjuice?style=for-the-badge&logo=pypi&logoColor=fff)](https://pypi.org/project/helpjuice/)
[![Python](https://img.shields.io/pypi/pyversions/helpjuice?style=for-the-badge&logo=python&logoColor=fff)](https://pypi.org/project/helpjuice/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge&logo=gnu&logoColor=fff)](https://www.gnu.org/licenses/gpl-3.0)
[![Tests](https://img.shields.io/github/workflow/status/samamorgan/helpjuice/Python%20%F0%9F%90%8D%20package%20%F0%9F%93%A6%20test?style=for-the-badge&logo=githubactions&logoColor=fff&label=Tests)](https://github.com/samamorgan/helpjuice/actions)
[![Codecov](https://img.shields.io/codecov/c/gh/samamorgan/helpjuice?logo=codecov&logoColor=fff&style=for-the-badge)](https://codecov.io/gh/samamorgan/helpjuice)
[![Docs](https://img.shields.io/readthedocs/helpjuice?logo=readthedocs&logoColor=fff&style=for-the-badge)](https://helpjuice.readthedocs.io/)

This package allows Python developers to write software that makes use of the Helpjuice API. Functions available in the API are mirrored in this package as closely as possible, translating JSON responses to Python objects. You can find the current documentation for the Helpjuice API here:

[Helpjuice API Documentation](https://help.helpjuice.com/en_US/api-v3/)

### Installing

```
pip install helpjuice
```

### Quick Start

```python
from helpjuice import Client

helpjuice = Client(account="your-account", api_key="ffb722a62e8**********************")

# Get a single article
article = helpjuice.Article(id=1).get()

# Search for articles with pagination
for question in helpjuice.Search().get(query="foo", limit=1000, paginate=True):
    print(question)
```
