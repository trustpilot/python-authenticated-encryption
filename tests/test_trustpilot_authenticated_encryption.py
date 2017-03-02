from trustpilot_authenticated_encryption import encrypt

def test():
    message = 'this is the secret message'
    encrypt_key = "g9hH6MkVnlKlGa5IG+5R/uKgyrCJxOsh5fXlwK0mjH0="
    hash_key = "oGmd/bHHkd+N6P6lZQxyfikjU7c5P/mhWO/noCsERyY="
    encrypted = encrypt(message.encode("utf-8"), encrypt_key, hash_key)

    assert len(encrypted.decode("ascii")) == 108
