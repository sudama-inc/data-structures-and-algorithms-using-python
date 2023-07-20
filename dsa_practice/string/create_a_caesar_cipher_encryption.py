"""
25. Write a Python program to create a Caesar encryption.

https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/

             
(Encryption Phase with shift n) : E_n(x)=(x+n)mod\26                 
(Decryption Phase with shift n) : D_n(x)=(x-n)mod\26
"""

# A python program to illustrate Caesar Cipher Technique


def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# check the above function
text = "ATTACKATONCE"
s = 4
print(encrypt(text, s))
