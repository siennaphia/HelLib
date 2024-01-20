from seal import (
    EncryptionParameters,
    scheme_type,
    Plaintext,
    Ciphertext,
    KeyGenerator,
    Encryptor,
)


def encrypt_message(message, public_key):
    # Create encryption parameters
    parms = EncryptionParameters(scheme_type.BFV)

    # Set parameters for the encryption scheme
    poly_modulus_degree = 4096
    parms.set_poly_modulus_degree(poly_modulus_degree)
    parms.set_coeff_modulus([60, 40, 40, 60])
    parms.set_plain_modulus(1 << 8)

    # Create key generator
    keygen = KeyGenerator(parms)
    public_key = keygen.public_key()

    # Create encryptor
    encryptor = Encryptor(parms, public_key)

    # Create a plaintext object and encode the message
    plaintext = Plaintext()
    plaintext.set_int(message)

    # Create a ciphertext and encrypt the plaintext
    ciphertext = Ciphertext()
    encryptor.encrypt(plaintext, ciphertext)

    return ciphertext


# Example usage:
# message_to_encrypt = 42
# public_key = None  #replace this with whatever  public key you use

# encrypted_result = encrypt_message(message_to_encrypt, public_key)
# print(f"Encrypted result: {encrypted_result}")
