import unittest
from trustpilot_authenticated_encryption.encryption import encrypt

class TestEncryption(unittest.TestCase):

    def test_encrypt_messagelength(self):
        message = 'this is the secret message'
        encrypt_key = "g9hH6MkVnlKlGa5IG+5R/uKgyrCJxOsh5fXlwK0mjH0="
        hash_key = "oGmd/bHHkd+N6P6lZQxyfikjU7c5P/mhWO/noCsERyY="
        encrypted = encrypt(message.encode("utf-8"), encrypt_key, hash_key)

        self.assertEqual(len(encrypted.decode("ascii")), 108)
