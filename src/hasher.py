import bcrypt

def hash_password(password):
    # Generate a salt for the password
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Return the hashed password as a string
    return hashed_password.decode('utf-8')
print(hash_password(input()))