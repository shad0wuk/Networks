from secrets import token_bytes
from Cryptodome.Cipher import AES


def decrypt():
    with open("plaintext.enc", "r") as f:
        cipher_material = eval(f.read())
        count = 3
        cipher_key = ""
        while cipher_key == "":
            if count != 0:
                cipher_key = input(
                    f"Enter cipher key (you have {count} tries left): ")
                try:
                    aes_cipher = AES.new(bytes.fromhex(cipher_key), AES.MODE_CBC, 
                                    iv=bytes.fromhex(cipher_material['iv']))
                    decrypted = aes_cipher.decrypt(bytes.fromhex(cipher_material['ciphertext']))
                
                    while decrypted[-1] == 0:
                        decrypted = decrypted[:-1]
                except ValueError:
                    print("Invalid cipher key")
                    count -= 1
                    cipher_key = ""
            else:
                print("Too many failed attempts")
                exit()
   
    with open("plaintext.dec", "w") as f:
        f.write(str(decrypted.decode()))
