import hashlib
import sys
import secrets

salt=secrets.token_bytes(8)
 
print((hashlib.pbkdf2_hmac('sha512', sys.argv[0].strip().encode(), salt, 200000)).hex())
