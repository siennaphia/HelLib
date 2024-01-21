from seal import Ciphertext, Decryptor, Encryptor, EncryptionParameters, Evaluator, IntegerEncoder, KeyGenerator, Plaintext, SEALContext

def generate_keys(context):
    keygen = KeyGenerator(context)
    public_key = keygen.public_key()
    secret_key = keygen.secret_key()
    return public_key, secret_key

def encrypt_data(data, public_key, encryptor, encoder):
    plaintext = Plaintext()
    encoder.encode(data, plaintext)
    ciphertext = Ciphertext()
    encryptor.encrypt(plaintext, ciphertext)
    return ciphertext

def decrypt_data(ciphertext, secret_key, decryptor, encoder):
    decrypted_data = Plaintext()
    decryptor.decrypt(ciphertext, decrypted_data)
    return encoder.decode_int64(decrypted_data)

def secure_aggregation(ciphertexts, evaluator, encryptor, decryptor, encoder):
    result_ciphertext = Ciphertext()
    evaluator.add_many(ciphertexts, result_ciphertext)
    
    # you can perform additional operations on the result_ciphertext
    
    # Decrypt the aggregated result
    result_plain = Plaintext()
    decryptor.decrypt(result_ciphertext, result_plain)
    
    return encoder.decode_int64(result_plain)

# Generate keys
public_key, secret_key = generate_keys(context)

# Create encryptor and decryptor
encryptor = Encryptor(context, public_key)
decryptor = Decryptor(context, secret_key)

# Create evaluator
evaluator = Evaluator(context)

# Create integer encoder with the plain modulus
encoder = IntegerEncoder(context.plain_modulus())

# Example data from different sources
data_sources = [42, 18, 56, 29]

# Encrypt data from different sources
ciphertexts = [encrypt_data(data, public_key, encryptor, encoder) for data in data_sources]

# Perform secure aggregation
result = secure_aggregation(ciphertexts, evaluator, encryptor, decryptor, encoder)

print("Original data:", data_sources)
print("Aggregated result:", result)
