from linmodel import LinModel
from seal import *
import os

def getData(context, filename):
    data = Ciphertext()
    data.load(context, filename)
    print("Loaded " + filename)
    return data

def computeData(context):
    scale = pow(2.0, 60)
    data = []
    for filename in (os.listdir("data")):
        data.append(getData(context, "data/" + filename))
    lm = LinModel()
    coeff = lm.getCoef()
    encoder = CKKSEncoder(context)

    plain_coeff = []
    
    for i in range (len(coeff)):
        plaintext = Plaintext()
        encoder.encode(coeff[i], scale, plaintext)
        plain_coeff.append(plaintext)

    cipher_coeff = []
    public_key = PublicKey()
    public_key.load(context, "keys/public.key")
    encoder = CKKSEncoder(context)
    encr = Encryptor(context, public_key)
    
    for i in range (len(coeff)):
        ciphertext = Ciphertext()
        encr.encrypt(plain_coeff[i], ciphertext)
        cipher_coeff.append(ciphertext)

    result = Ciphertext()

    eval = Evaluator(context)

    for i in range(len(data)):
        eval.multiply(data[i], cipher_coeff[i], data[i])
    for i in range(1, len(data)):
        eval.add(data[0], data[i], data[0])

    serializeData(data[0])

def serializeData(data):
    data.save("data/result")
    print("Saved result")


def main(context):
    computeData(context)
