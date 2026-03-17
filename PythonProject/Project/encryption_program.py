
import random
import string

# tạo bảng ký tự
chars = list(" " + string.ascii_letters + string.digits + string.punctuation)

key = chars.copy()
random.shuffle(key)

print("=== Decryption Program ===")
print(f"chars: {chars}")
print(f"key  : {key}")

# DECRYPT
cipher_text = input("\nEnter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    if letter in key:
        index = key.index(letter)
        plain_text += chars[index]
    else:
        plain_text += letter

print(f"\nencrypted message: {cipher_text}")
print(f"decrypted message: {plain_text}")