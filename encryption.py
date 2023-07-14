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
####################################################
    
a = input("Encrypt your message : ")
print("\nStage 1 \n")
process_message()
def encrypt(text, n):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + n - 65) % 26 + 65)
            else:
                result += chr((ord(char) + n - 97) % 26 + 97)
        else:
            result += char

    return result

n = 15
encrypted_message_1 = encrypt(a, n)
print("\nMESSAGE : ", encrypted_message_1)

print("STAGE 1 ENCRYPTION IS COMPLETED")
###################################################

print("\nStage 2 \n")
process_message()
def encrypt1(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += encrypted_char
        else:
            result += char
    return result



plaintext_2 = encrypted_message_1
encryption_shift = 3

encrypted_message2 = encrypt1(plaintext_2, encryption_shift)
print("\nMESSAGE : ", encrypted_message2)

################################

print("\nStage 3 \n")
process_message()
def encrypt_ascii(text):
    encrypted_values = []
    for char in text:
        ascii_value = ord(char)
        encrypted_values.append(ascii_value)
    return encrypted_values

plaintext_3 = encrypted_message2
encrypted_message_3 = encrypt_ascii(plaintext_3)
encrypted_message_3 = ' '.join(map(str, encrypted_message_3))

print("\nMESSAGE : ", encrypted_message_3)

print("STAGE 3 ENCRYPTION IS COMPLETED")
##########################################################
