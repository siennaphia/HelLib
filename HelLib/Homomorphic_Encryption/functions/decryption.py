from seal import (

    Plaintext,
    Decryptor,
)


def decrypt_message(ciphertext, secret_key):
    # Create decryptor
    decryptor = Decryptor(secret_key)

    # Create a plaintext to store the decrypted result
    decrypted_result = Plaintext()

    # Decrypt the ciphertext
    decryptor.decrypt(ciphertext, decrypted_result)

    # Return the decrypted result
    return decrypted_result.to_int()

# Example usage bellow
# Assuming you already have the public_key and secret_key
# public_key = ...  # Replace with your actual public key
# secret_key = ...  # Replace with your actual secret key

# # Encrypt a message
# encrypted_msg = encrypt_message(42, public_key)
# print("Encrypted Message:", encrypted_msg)

# # Decrypt the message
# decrypted_msg = decrypt_message(encrypted_msg, secret_key)
# print("Decrypted Message:", decrypted_msg)