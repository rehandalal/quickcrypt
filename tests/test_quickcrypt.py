import re

from quickcrypt import encrypt, decrypt


def test_encrypt():
    for i in range(100):
        encrypted = encrypt("test", "test")
        assert(re.match(r"^[258be]e8[258be]ca[258be]e6[258be]e8$", encrypted))


def test_decrypt():
    encrypted = "2e85ca8e6be8eddbd35da"
    assert decrypt(encrypted, "test") == "testing"
