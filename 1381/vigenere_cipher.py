def vigenere_encrypt(plaintext, key):
    result = ""
    key = key.lower()
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            key_shift = ord(key[i % key_length]) - 97
            result += chr((ord(char) - shift + key_shift) % 26 + shift)
        else:
            result += char
    return result

def vigenere_decrypt(ciphertext, key):
    result = ""
    key = key.lower()
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            key_shift = ord(key[i % key_length]) - 97
            result += chr((ord(char) - shift - key_shift + 26) % 26 + shift)
        else:
            result += char
    return result

if __name__ == "__main__":
    print("Vigenère Cipher")
    text = input("Enter text: ")
    key = input("Enter key: ")
    encrypted = vigenere_encrypt(text, key)
    print("Encrypted:", encrypted)
    print("Decrypted:", vigenere_decrypt(encrypted, key))
