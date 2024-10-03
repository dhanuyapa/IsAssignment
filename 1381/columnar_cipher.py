def columnar_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    rows = [plaintext[i:i+len(key)] for i in range(0, len(plaintext), len(key))]
    if len(rows[-1]) < len(key):
        rows[-1] += ' ' * (len(key) - len(rows[-1]))
    ciphertext = ''.join(''.join(rows[row][col] for row in range(len(rows))) for col in key_order)
    return ciphertext

def columnar_decrypt(ciphertext, key):
    num_rows = len(ciphertext) // len(key)
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    rows = [[''] * len(key) for _ in range(num_rows)]
    index = 0
    for col in key_order:
        for row in range(num_rows):
            rows[row][col] = ciphertext[index]
            index += 1
    plaintext = ''.join(''.join(row) for row in rows)
    return plaintext.rstrip()

if __name__ == "__main__":
    print("Columnar Cipher")
    text = input("Enter text: ")
    key = input("Enter key (e.g., 3124): ")
    encrypted = columnar_encrypt(text, key)
    print("Encrypted:", encrypted)
    print("Decrypted:", columnar_decrypt(encrypted, key))
