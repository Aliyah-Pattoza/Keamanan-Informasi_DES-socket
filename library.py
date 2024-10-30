import des
from time import sleep
import sys 

# Fungsi konversi dari binary ke ASCII
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

# Fungsi konversi dari ASCII ke binary
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

# Fungsi yang membagi string menjadi beberapa kelompok sesuai panjang yang diinginkan
def splitIntoGroups(string, length):
    return [string[i:i+length] for i in range(0, len(string), length)]

# Fungsi padding untuk memastikan panjang pesan kelipatan 8 bit
def pad_message(message):
    padding_length = 8 - (len(message) % 8)
    return message + '0' * padding_length if padding_length < 8 else message

# Fungsi encrypt untuk menggunakan padding
def encrypt(message):
    ki = des.DES()
    binary = text_to_bits(message)
    binary = pad_message(binary)
    entries = splitIntoGroups(binary, 8)
    encryptedEntries = [ki.Encryption(entry) for entry in entries]
    return "".join(encryptedEntries)

# Fungsi decrypt untuk menghilangkan padding
def decrypt(message):
    ki = des.DES()
    entries = splitIntoGroups(message, 8)
    decryptedMessages = [ki.Decryption(entry) for entry in entries]
    decryptedMessage = "".join(decryptedMessages).rstrip('0')  # Menghapus padding
    return text_from_bits(decryptedMessage)

# Fungsi menampilkan loading bar
def sending():
    print("\nSending ", end="")
    for _ in range(5):
        sleep(0.4)
        print(".", end="")
        sys.stdout.flush()
    print(' SENT')
