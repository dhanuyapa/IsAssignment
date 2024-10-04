def vigenere_encrypt(plaintext, key):
    result = ""
    key = key.lower()  # Ensure the key is in lowercase
    key_length = len(key)

    # Remove spaces from the plaintext
    plaintext = plaintext.replace(" ", "")  # Remove all spaces from the plaintext
    
    # Encrypt each character
    for i, char in enumerate(plaintext):
        if char.isalpha():  # Check if the character is a letter
            shift = 65 if char.isupper() else 97  # Adjust shift based on case (uppercase/lowercase)
            key_shift = ord(key[i % key_length]) - 97  # Calculate the shift from the key
            result += chr((ord(char) - shift + key_shift) % 26 + shift)  # Encrypt and add to result

    return result

if __name__ == "__main__":
    print("Vigenère Cipher - Encryption")
    text = input("Enter plaintext: ")
    key = input("Enter key: ")
    encrypted = vigenere_encrypt(text, key)
    print("Encrypted Text:", encrypted)
