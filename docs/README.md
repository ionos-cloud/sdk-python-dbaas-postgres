# Python SDK For IONOS Cloud Dbaas Postgres

## Overview

The IONOS Cloud SDK for Python provides you with access to the IONOS Cloud Dbaas Postgres API.

## Getting Started

An IONOS account is required for access to the Dbaas Postgres API; credentials from your registration are used to authenticate against the IONOS Cloud API.

### Installation & Usage

**Requirements:**
- Python >= 3.5

### pip install

Since this package is hosted on PyPI \([https://pypi.org/](https://pypi.org/)\) you can install it like this

```bash
pip install ionoscloud_dbaas_postgres
```

If the python package is hosted on a repository, you can install directly using:

```bash
pip install git+https://github.com/ionos-cloud/sdk-python-dbaas-postgres.git
```

\(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ionos-cloud/sdk-python-dbaas-postgres.git`\)

Then import the package:

```python
import ionoscloud_dbaas_postgres
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```bash
python setup.py install --user
```

\(or `sudo python setup.py install` to install the package for all users\)

Then import the package:

```python
import ionoscloud_dbaas_postgres
```

> **_NOTE:_**  The Python SDK does not support Python 2. It only supports Python >= 3.5.


### Authentication

The username and password or the authentication token can be manually specified when initializing the SDK client:

```python
configuration = ionoscloud_dbaas_postgres.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)
client = ionoscloud_dbaas_postgres.ApiClient(configuration)
```

Environment variables can also be used; the SDK uses the following variables:

* IONOS\_USERNAME - to specify the username used to login
* IONOS\_PASSWORD - to specify the password
* IONOS\_TOKEN - if an authentication token is being used

**Warning**: Make sure to follow the Information Security Best Practices when using credentials within your code or storing them in a file.

## FAQ

1. How can I open a bug/feature request? 

Bugs & feature requests can be open on the repository issues: [https://github.com/ionos-cloud/sdk-python-dbaas-postgres/issues/new/choose](https://github.com/ionos-cloud/sdk-python-dbaas-postgres/issues/new/choose)

2. Can I contribute to the Python SDK?

Pure SDKs are automatically generated using OpenAPI Generator and don’t support manual changes. If you need changes please open an issue and we’ll try to take care of it.

