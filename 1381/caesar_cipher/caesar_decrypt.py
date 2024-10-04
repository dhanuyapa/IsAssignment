def columnar_decrypt(ciphertext, key):
    # Calculate the number of rows
    num_rows = len(ciphertext) // len(key)
    
    # Create the order of the columns based on the numerical key
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    
    # Create an empty matrix for rows
    rows = [[''] * len(key) for _ in range(num_rows)]

    # Fill the matrix with the characters from the ciphertext based on the key order
    index = 0
    for col in key_order:
        for row in range(num_rows):
            rows[row][col] = ciphertext[index]
            index += 1

    # Reconstruct the plaintext by reading row by row
    plaintext = ''.join(''.join(row) for row in rows)
    
   
    
    # Remove padding 'X' characters added during encryption and convert to lowercase
    final_plaintext = plaintext.rstrip('X').lower()
    


    return final_plaintext

if __name__ == "__main__":
    print("Columnar Cipher - Decryption")
    ciphertext = input("Enter ciphertext: ")
    key = input("Enter key (e.g., 3124): ")
    decrypted = columnar_decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted)
