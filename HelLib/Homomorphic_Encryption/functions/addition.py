from seal import (
    EncryptionParameters,
    scheme_type,
    Plaintext,
    Ciphertext,
    KeyGenerator,
    Encryptor,
    Evaluator,
)


def homomorphic_addition(ciphertext1, ciphertext2, public_key):
    # Create encryption parameters (assuming the same parameters used for both ciphertexts)
    parms = ciphertext1.parms_id()

    # Create key generator
    keygen = KeyGenerator(parms)
    public_key = keygen.public_key()

    # Create an evaluator
    evaluator = Evaluator(parms)

    # Create a new ciphertext for the result
    result_ciphertext = Ciphertext()

    # Perform homomorphic addition
    evaluator.add(ciphertext1, ciphertext2, result_ciphertext)

    return result_ciphertext


# Example usage:
# ciphertext1 = ...  # Replace with your actual ciphertext 1
# ciphertext2 = ...  # Replace with your actual ciphertext 2
# public_key = None  # Replace with your actual public key

# result = homomorphic_addition(ciphertext1, ciphertext2, public_key)
# print(f"Result of homomorphic addition: {result}")
