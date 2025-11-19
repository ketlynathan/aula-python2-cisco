import cv2
from pyzbar.pyzbar import decode
import webbrowser
import time


def main():
    # Inicializa a webcam (0 = webcam padrão)
    cap = cv2.VideoCapture(0)
    found_qr = None

    print("🕵️‍♂️ Aponte a câmera para o QR Code...")

    while True:
        # Captura o frame da webcam
        ret, frame = cap.read()
        if not ret:
            print("Erro ao acessar a webcam.")
            break

        # Decodifica qualquer QR encontrado
        for qr in decode(frame):
            data = qr.data.decode('utf-8')
            found_qr = data
            # Desenha um retângulo ao redor do QR
            (x, y, w, h) = qr.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(frame, "QR Detectado!", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Mostra o vídeo em tempo real
        cv2.imshow("Leitor de QR Code", frame)

        # Se o QR foi detectado, abre o link e sai
        if found_qr:
            print(f"✅ QR Code detectado: {found_qr}")
            if found_qr.startswith("http"):
                print("🌐 Abrindo URL no navegador...")
                webbrowser.open(found_qr)
            else:
                print("🔎 Conteúdo não é uma URL:", found_qr)
            time.sleep(2)
            break

        # Pressione 'q' para sair manualmente
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera recursos
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
