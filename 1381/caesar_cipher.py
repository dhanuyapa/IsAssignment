def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

if __name__ == "__main__":
    print("Caesar's Cipher")
    text = input("Enter text: ")
    key = int(input("Enter key: "))
    encrypted = caesar_encrypt(text, key)
    print("Encrypted:", encrypted)
    print("Decrypted:", caesar_decrypt(encrypted, key))
