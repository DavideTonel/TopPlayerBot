import hashlib

def hash_password(password):
    # Hash password using SHA-256 algorithm
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


print(hash_password(input()))