import re

from quickcrypt import encrypt, decrypt


def test_encrypt():
    for i in range(100):
        encrypted = encrypt("test", "test")
        assert(re.match(
            r"^([258be]|[369cf]0)e8([258be]|[369cf]0)ca([258be]|[369cf]0)e6([258be]|[369cf]0)e8$",
            encrypted
        ))


def test_decrypt():
    encrypted = "2e85ca8e6be8edd30d360da"
    assert decrypt(encrypted, "test") == "testing"
