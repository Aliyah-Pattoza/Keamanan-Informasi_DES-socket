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
        mySocket.send(encryptedMessage.encode())

    mySocket.close()
    print("Connection closed by client.")

if __name__ == '__main__':
    Main()
