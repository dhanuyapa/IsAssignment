def vigenere_decrypt(ciphertext, key):
    result = ""
    key = key.lower()  # Ensure the key is in lowercase
    key_length = len(key)
    key_index = 0  # Track which letter of the key to use

    for char in ciphertext:
        if char.isalpha():  # Apply key only to alphabetic characters
            shift = 65 if char.isupper() else 97  # Adjust shift based on case (uppercase/lowercase)
            key_shift = ord(key[key_index % key_length]) - 97  # Calculate the shift from the key
            result += chr((ord(char) - shift - key_shift + 26) % 26 + shift)  # Decrypt and add to result
            key_index += 1  # Move to the next letter in the key
        else:
            result += char  # Non-alphabetic characters (e.g., spaces) remain unchanged

    return result

if __name__ == "__main__":
    print("Vigenère Cipher - Decryption")
    ciphertext = input("Enter ciphertext: ")
    key = input("Enter key: ")
    decrypted = vigenere_decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted)
