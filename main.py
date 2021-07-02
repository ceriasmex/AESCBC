# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def cipher(name):
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    import os

    key = os.urandom(32)
    iv = os.urandom(16)

    aesCipher = Cipher(algorithms.AES(key),
                       modes.CBC(iv),
                       backend=default_backend())
    aesEncryptor = aesCipher.encryptor()
    aesDecryptor = aesCipher.decryptor()

    # Use a breakpoint in the code line below to debug your script.
    print(iv)
    print(aesEncryptor)
    print(aesDecryptor)
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cipher('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
