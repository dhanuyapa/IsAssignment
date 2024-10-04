def rail_fence_decrypt(ciphertext, key):
    # Create a matrix to mark the zigzag pattern
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(key)]
    row, direction = 0, 1
    
    # Mark the positions of the characters in the zigzag pattern
    for i in range(len(ciphertext)):
        rail[row][i] = '*'
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1

    # Fill the matrix with the characters from the ciphertext
    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    # Reconstruct the plaintext by following the zigzag pattern
    result = []
    row, direction = 0, 1
    for i in range(len(ciphertext)):
        result.append(rail[row][i])
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1

    return ''.join(result)

if __name__ == "__main__":
    print("Rail Fence Cipher - Decryption")
    ciphertext = input("Enter ciphertext: ")
    key = int(input("Enter key (number of rails): "))
    decrypted = rail_fence_decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted)
