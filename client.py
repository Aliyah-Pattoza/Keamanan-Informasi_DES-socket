import socket
import library

def Main():
    host = "127.0.0.1"
    port = 5001

    # Inisialisasi koneksi ke server
    mySocket = socket.socket()
    mySocket.connect((host, port))

    while True:
        # Mengambil input pesan dari client
        message = input("Enter the message you want to send (or 'q' to quit): ")
        if message.lower() == 'q':
            mySocket.send(message.encode())
            break

        # Enkripsi pesan sebelum dikirim
        encryptedMessage = library.encrypt(message)
        print("Encrypted message to be sent:", encryptedMessage)
        
        # Kirim pesan terenkripsi ke server
        library.sending()
        mySocket.send(encryptedMessage.encode())
        
        # Menerima pesan terenkripsi dari server
        data = mySocket.recv(1024).decode()
        if not data or data.lower() == 'q':
            print("Connection closed by server.")
            break

        # Dekripsi pesan yang diterima
        decryptedMessage = library.decrypt(data)
        print("Received Encrypted Message:", data)
        print("Decrypted Message:", decryptedMessage)
        print("\n")
    
    mySocket.close()
    print("Connection closed by client.")

if __name__ == '__main__':
    Main()
