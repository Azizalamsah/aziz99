def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

if __name__ == "__main__":
    text = input("Masukkan teks yang ingin dienkripsi: ")
    shift = int(input("Masukkan nilai pergeseran (shift): "))

    encrypted = caesar_encrypt(text, shift)
    print(f"Teks terenkripsi: {encrypted}")

    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Teks terdekripsi: {decrypted}")
