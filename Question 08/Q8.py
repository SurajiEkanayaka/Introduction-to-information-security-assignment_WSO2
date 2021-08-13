import hashlib
import sys
import secrets

salt=secrets.token_bytes(8)
hash = hashlib.sha512( str( salt ).encode("utf-8") ).hexdigest()
print(hash)
