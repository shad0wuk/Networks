from secrets import token_bytes
from Cryptodome.Cipher import AES

def encrypt(string):
    plaintext = string.encode('utf-8')
    while len(plaintext) % 16 != 0:
        plaintext += b'\x00'
    aes_key = token_bytes(16)
    aes_cipher = AES.new(aes_key, AES.MODE_CBC)
    ciphertext = aes_cipher.encrypt(plaintext)
    cipher_material = {
        'key': aes_key.hex(),
        'iv': aes_cipher.iv.hex(),
        'ciphertext': ciphertext.hex()
    }

    return cipher_material