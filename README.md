# Trustpilot authenticated encryption for python

Library for authenticated encryption used with Trustpilot.

## Install
- `pip install git+https://github.com/trustpilot/python-authenticated-encryption@1.0.0`
- Omit @{version} at the end to install the latest source version

## Usage
To encrypt a message

```
from trustpilot_authenticated_encryption import encryption

message = 'this is the secret message'
encrypt_key = "g9hH6MkVnlKlGa5IG+5R/uKgyrCJxOsh5fXlwK0mjH0="
hash_key = "oGmd/bHHkd+N6P6lZQxyfikjU7c5P/mhWO/noCsERyY="
encrypted_message = encryption.encrypt(message.encode("utf-8"), encrypt_key, hash_key)
```
