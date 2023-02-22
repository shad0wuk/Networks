from encrypt import encrypt
from decrypt import decrypt

def main():
    plaintext = input("Enter a string to encrypt: ")
    cipher_material = encrypt(plaintext)
    print(f"Cipher material: {cipher_material}")

    decrypted_text = decrypt(cipher_material)
    print(f"Plaintext: {decrypted_text}")

if __name__ == "__main__":
    main()