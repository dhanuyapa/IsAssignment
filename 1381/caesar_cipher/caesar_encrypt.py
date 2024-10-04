def caesar_encrypt(plaintext, key):
    result = ""
    
    # Convert plaintext to uppercase
    plaintext = plaintext.upper()

    for char in plaintext:
        if char.isalpha():
            shift = 65  # 'A' = 65, because we are working only with uppercase letters
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char  # Non-alphabetic characters remain unchanged

    return result

if __name__ == "__main__":
    print("Caesar's Cipher - Encryption")
    text = input("Enter plaintext: ")
    key = int(input("Enter key: "))
    encrypted = caesar_encrypt(text, key)
    print("Encrypted Text:", encrypted)
