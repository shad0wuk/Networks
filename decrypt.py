from secrets import token_bytes
from Cryptodome.Cipher import AES

def decrypt(cipher_material):
    aes_cipher = AES.new(bytes.fromhex(cipher_material['key']), AES.MODE_CBC, 
                         iv=bytes.fromhex(cipher_material['iv']))
    decrypted = aes_cipher.decrypt(bytes.fromhex(cipher_material['ciphertext']))
    
    while decrypted[-1] == 0:
        decrypted = decrypted[:-1]

    return decrypted.decode()
