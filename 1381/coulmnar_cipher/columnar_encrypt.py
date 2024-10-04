def columnar_encrypt(plaintext, key):
    # Remove spaces and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()
    
    # Create key order based on the numerical value of the key
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    
    # Split the plaintext into rows based on the length of the key
    rows = [plaintext[i:i + len(key)] for i in range(0, len(plaintext), len(key))]
    
    # If the last row is shorter, pad it with spaces
    if len(rows[-1]) < len(key):
        rows[-1] += ' ' * (len(key) - len(rows[-1]))

    # Generate the ciphertext by reading columns based on the key order
    ciphertext = ''.join(''.join(rows[row][col] for row in range(len(rows))) for col in key_order)
    
    return ciphertext

if __name__ == "__main__":
    print("Columnar Cipher - Encryption")
    text = input("Enter plaintext: ")
    key = input("Enter key (e.g., 3124): ")
    encrypted = columnar_encrypt(text, key)
    print("Encrypted Text:", encrypted)
