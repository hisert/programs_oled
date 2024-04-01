import socket
import threading
import signal
import sys

def handle_client(client_socket, client_address):
    print(f"{client_address} adresinden bağlantı kabul edildi.")

    while True:
        # İstemciden gelen veriyi al
        data = client_socket.recv(1024)
        if not data:
            break
        received_message = data.decode()
        print(f"Alınan veri: {received_message}")

        # İstemciye cevap gönder
        response = "Veri alındı. Teşekkürler!"
        client_socket.sendall(response.encode('utf-8'))

    # Bağlantıyı kapat
    client_socket.close()
    print(f"{client_address} adresinden bağlantı kapatıldı.")

def main():
    # Sunucu soketini oluştur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12346))  # Tüm ağ arayüzlerinden gelen bağlantıları kabul et
    server_socket.listen(5)

    print("Sunucu başlatıldı. İstemci bekleniyor...")

    # Ctrl+C ile sunucuyu kapatmak için sinyal işleyici ekle
    def signal_handler(sig, frame):
        print("Ctrl+C ile sunucu kapatılıyor...")
        server_socket.close()
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        # Bağlantıyı kabul et
        client_socket, client_address = server_socket.accept()

        # İstemciye hizmet vermek için yeni bir iş parçacığı oluştur
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()
Bu güncellenmiş
