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
        'iv': aes_cipher.iv.hex(),
        'ciphertext': ciphertext.hex()
    }

    cipher_key = aes_key.hex()

    print(f"Cipher key: {cipher_key}")

    with open("plaintext.enc", "w") as f:
        f.write(str(cipher_material))
