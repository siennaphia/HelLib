import seal
from seal import (Ciphertext,
                 Decryptor,
                 Encryptor,
                 EncryptionParameters,
                 Evaluator,
                 IntegerEncoder,
                 KeyGenerator,
                 Plaintext,
                 SEALContext)

def homomorphic_exponentiation(encrypted, exponent, evaluator):
    result = Ciphertext(encrypted)
    for _ in range(exponent-1):
        evaluator.multiply(result, encrypted)
    return result
