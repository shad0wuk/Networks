from encrypt import encrypt
from decrypt import decrypt


def main():
    with open("plaintext.txt", "r") as f:
        plaintext = f.read()
    encrypt(plaintext)
    # print(f"Cipher material: {cipher_material}")

    decrypt()
    print("Decryption successful")


if __name__ == "__main__":
    main()
