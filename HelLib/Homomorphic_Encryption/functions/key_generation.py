from seal import (
    KeyGenerator,
)

def KeyGenerator(context):
    # public key and secret key generated from KeyGeneratoer 
    keygen = KeyGenerator(context)
    public_key = keygen.public_key()
    secret_key = keygen.secret_key()

    return public_key,secret_key

