import time

def process_message():
    print("                Processing", end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)

def decrypt(text, n):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - n - 65) % 26 + 65)
            else:
                result += chr((ord(char) - n - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt1(encrypted_text, shift):
    result = ""
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift + 26) % 26 + ascii_offset)
            result += decrypted_char
        else:
            result += char
    return result

def decrypt_ascii(encrypted_values):
    decrypted_text = ""
    for value in encrypted_values:
        char = chr(value)
        decrypted_text += char
    return decrypted_text


################################################################
encrypted_message_3 = input("Enter your encrypted message : ")
encrypted_message_3 = list(map(int, encrypted_message_3.split()))

encryption_shift = 3
print("\nStage 1 \n")
process_message()
decrypted_message_3 = decrypt_ascii(encrypted_message_3)
print("\nMESSAGE :", decrypted_message_3)
print("STAGE 1 DECRYPTION IS COMPLETED")
################################################################

print("\nStage 2 \n")
process_message()
plaintext_2 = decrypt1(decrypted_message_3, encryption_shift)
print("\nMESSAGE :", plaintext_2)
print("STAGE 2 DECRYPTION IS COMPLETED")
################################################################

print("\nStage 3 \n")
process_message()
decrypted_message_2 = decrypt(plaintext_2, 15)
print("\nMESSAGE :", decrypted_message_2)
print("STAGE 3 DECRYPTION IS COMPLETED")
################################################################
