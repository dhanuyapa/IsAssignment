def rail_fence_encrypt(plaintext, key):
    # Remove spaces from the plaintext and initialize the rails
    plaintext = plaintext.replace(" ", "")
    rail = [''] * key
    row, direction = 0, 1  # Starting row and direction
    
    # Iterate over each character in the plaintext
    for char in plaintext:
        # Append the character to the appropriate rail
        rail[row] += char
        row += direction  # Move to the next row

        # Reverse the direction when we reach the top or bottom rail
        if row == 0 or row == key - 1:
            direction *= -1

    # Return the encrypted text by joining all rails
    return ''.join(rail)

if __name__ == "__main__":
    print("Rail Fence Cipher - Encryption")
    text = input("Enter plaintext: ")
    key = int(input("Enter key (number of rails): "))
    encrypted = rail_fence_encrypt(text, key)
    print("Encrypted Text:", encrypted)
