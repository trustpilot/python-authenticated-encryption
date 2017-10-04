# Trustpilot authenticated encryption for python

[![Build Status](http://travis-ci.org/trustpilot/python-authenticated-encryption.svg?branch=master)](https://travis-ci.org/trustpilot/python-authenticated-encryption)  [![Latest Version](https://img.shields.io/pypi/v/trustpilot_authenticated_encryption.svg)](https://pypi.python.org/pypi/trustpilot_authenticated_encryption) [![Python Support](https://img.shields.io/pypi/pyversions/trustpilot_authenticated_encryption.svg)](https://pypi.python.org/pypi/trustpilot_authenticated_encryption)

Library for authenticated encryption used with Trustpilot.

## Install

```
pip install trustpilot_authenticated_encryption
```

## Usage
To encrypt a message

```
from trustpilot_authenticated_encryption import encryption

message = 'this is the secret message'
encrypt_key = "g9hH6MkVnlKlGa5IG+5R/uKgyrCJxOsh5fXlwK0mjH0="
hash_key = "oGmd/bHHkd+N6P6lZQxyfikjU7c5P/mhWO/noCsERyY="
encrypted_message = encryption.encrypt(message.encode("utf-8"), encrypt_key, hash_key)
```
