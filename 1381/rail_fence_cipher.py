def rail_fence_encrypt(plaintext, key):
    rail = [''] * key
    row, direction = 0, 1
    for char in plaintext:
        rail[row] += char
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    return ''.join(rail)

def rail_fence_decrypt(ciphertext, key):
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(key)]
    row, direction = 0, 1
    for i in range(len(ciphertext)):
        rail[row][i] = '*'
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1

    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    result = []
    row, direction = 0, 1
    for i in range(len(ciphertext)):
        result.append(rail[row][i])
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    return ''.join(result)

if __name__ == "__main__":
    print("Rail Fence Cipher")
    text = input("Enter text: ")
    key = int(input("Enter key (number of rails): "))
    encrypted = rail_fence_encrypt(text, key)
    print("Encrypted:", encrypted)
    print("Decrypted:", rail_fence_decrypt(encrypted, key))
