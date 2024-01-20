from seal import (
    EncryptionParameters,
    scheme_type,
    Plaintext,
    Ciphertext,
    KeyGenerator,
    Encryptor,
)

def KeyGenerator(context):
    # public key and secret generated from KeyGeneratoer 
    keygen = KeyGenerator(context)
    public_key = keygen.public_key()
    secret_key = keygen.secret_key()

    return public_key,secret_key


