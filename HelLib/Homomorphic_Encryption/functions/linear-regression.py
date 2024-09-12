import pandas as pd
import seal
from seal import EncryptionParameters, SEALContext, IntegerEncoder, KeyGenerator, Encryptor, Decryptor, Evaluator,Ciphertext,Plaintext


def init_seal():
    # Set the polynomial modulus and the coefficient modulus
    poly_modulus = "1x^2048 + 1"
    coeff_modulus = seal.coeff_modulus_128(2048)
    plain_modulus = 256

    params = EncryptionParameters()
    params.set_poly_modulus(poly_modulus)
    params.set_coeff_modulus(coeff_modulus)
    params.set_plain_modulus(plain_modulus)

    context = SEALContext(params)
    return context

def load_and_preprocess_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Use 'age' as input and 'salary' as output (modify as needed)
    df = df[['age', 'salary']].head(10)
    return df

def encrypt_data(data, encoder, encryptor):
    encrypted_data = []
    for value in data:
        plain = encoder.encode(value)
        encrypted = Ciphertext()
        encryptor.encrypt(plain, encrypted)
        encrypted_data.append(encrypted)
    return encrypted_data

def decrypt_data(encrypted_data, decryptor, encoder):
    decrypted_data = []
    for encrypted in encrypted_data:
        plain = Plaintext()
        decryptor.decrypt(encrypted, plain)
        decrypted_data.append(encoder.decode_int32(plain))
    return decrypted_data

def homomorphic_linear_regression(encrypted_data, m, b, encoder, evaluator, encryptor):
    # Encrypt the coefficients
    plain_m = Plaintext()
    plain_b = Plaintext()
    encoder.encode(m, plain_m)
    encoder.encode(b, plain_b)

    encrypted_m = Ciphertext()
    encrypted_b = Ciphertext()
    encryptor.encrypt(plain_m, encrypted_m)
    encryptor.encrypt(plain_b, encrypted_b)

    # Perform the calculation y = mx + b homomorphically
    encrypted_y = []
    for encrypted_x in encrypted_data:
        encrypted_mx = Ciphertext()
        evaluator.multiply_plain(encrypted_x, plain_m, encrypted_mx)  # Use plain_m
        encrypted_yx = Ciphertext()
        evaluator.add(encrypted_mx, encrypted_b, encrypted_yx)  # Use encrypted_b
        encrypted_y.append(encrypted_yx)

    return encrypted_y

def example():
    # Initialize SEAL components
    context = init_seal()
    encoder = IntegerEncoder(context.plain_modulus())
    keygen = KeyGenerator(context)
    public_key = keygen.public_key()
    secret_key = keygen.secret_key()
    encryptor = Encryptor(context, public_key)
    decryptor = Decryptor(context, secret_key)
    evaluator = Evaluator(context)  # Create an instance of Evaluator

    # Load the dataset
    file_path = 'employee_data.csv'
    df = pd.read_csv(file_path)
    
    ages = df['age'].tolist()


    # Encrypt all columns in the dataset
    encrypted_columns = {}
    for column in df.columns:
        encrypted_columns[column] = encrypt_data(df[column].astype(int).tolist(), encoder, encryptor)
    
    
    # Perform homomorphic linear regression
    m = 2  # slope
    b = 3  # intercept
    encrypted_y = homomorphic_linear_regression(encrypted_columns['age'], m, b, encoder, evaluator, encryptor)
    
    # Decrypt the results
    decrypted_y = decrypt_data(encrypted_y, decryptor, encoder)
    
    
    # Check if lengths match
    if len(ages) != len(decrypted_y):
        print("Error: Length mismatch between ages and decrypted results")
        print("Length of ages:", len(ages))
        print("Length of decrypted results:", len(decrypted_y))
        return

    # Plotting
    plt.scatter(ages, decrypted_y, color='blue', label='Homomorphic Linear Regression')
    plt.xlabel('Age')
    plt.ylabel('Salary (Decrypted Predictions)')
    plt.title('Homomorphic Linear Regression on Employee Data')
    plt.legend()
    plt.show()
    

example()

