from seal import (
    KeyGenerator,
)

def Key_generator(context):
    #  public key and secret key generated from KeyGenerator
    keygen = KeyGenerator(context)
    public_key = keygen.public_key()
    secret_key = keygen.secret_key()

    return public_key,secret_key

