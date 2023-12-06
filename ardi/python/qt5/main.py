from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from desain import Ui_Form
from PIL import Image


class ImageEncryptionApp(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Buat atribut untuk menyimpan gambar
        self.original_image = None
        self.encrypted_image = None

        # Connect the signals to slots
        self.pushButton_4.clicked.connect(self.upload_image)
        self.pushButton_2.clicked.connect(self.encrypt_image)
        self.pushButton_3.clicked.connect(self.decrypt_image)
        self.pushButton.clicked.connect(self.save_file)

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image File", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            self.original_image = Image.open(file_path)
            self.original_image = self.original_image.resize(
                (201, 191), Image.LANCZOS)

            # Convert PIL Image to QImage
            q_image = QImage(self.original_image.tobytes(), self.original_image.width, self.original_image.height,
                             self.original_image.width * 3, QImage.Format_RGB888)

            # Convert QImage to QPixmap
            pixmap = QPixmap.fromImage(q_image)
            self.frame_3.setPixmap(pixmap)

    def encrypt_image(self):
        key = self.lineEdit.text().upper()

        # Convert key to bytes
        key_bytes = key.encode('utf-8')

        # Step 1: Beaufort Cipher
        beaufort_cipher = bytearray()
        for i in range(len(self.original_image.tobytes())):
            char_original = self.original_image.tobytes()[i]
            char_key = key_bytes[i % len(key_bytes)]
            char_cipher = (char_key - char_original) % 256
            beaufort_cipher.append(char_cipher)

        # Step 2: Vigenere Cipher
        vigenere_cipher = bytearray()
        for i in range(len(beaufort_cipher)):
            char_original = beaufort_cipher[i]
            char_key = key_bytes[i % len(key_bytes)]
            char_cipher = (char_original + char_key) % 256
            vigenere_cipher.append(char_cipher)

        # Create a new PIL Image from the encrypted bytes
        encrypted_image = Image.frombytes(
            "RGB", self.original_image.size, bytes(vigenere_cipher))

        # Convert PIL Image to QImage
        q_image = QImage(encrypted_image.tobytes(), encrypted_image.width, encrypted_image.height,
                         encrypted_image.width * 3, QImage.Format_RGB888)

        # Convert QImage to QPixmap
        pixmap = QPixmap.fromImage(q_image)
        self.frame_4.setPixmap(pixmap)

        # Set the encrypted image attribute
        self.encrypted_image = encrypted_image

    def decrypt_image(self):
        key = self.lineEdit.text().upper()

        # Convert key to bytes
        key_bytes = key.encode('utf-8')

        # Step 1: Beaufort Cipher
        beaufort_cipher = bytearray()
        for i in range(len(self.original_image.tobytes())):
            char_original = self.original_image.tobytes()[i]
            char_key = key_bytes[i % len(key_bytes)]
            char_cipher = (char_key + char_original) % 256
            beaufort_cipher.append(char_cipher)

        # Step 2: Vigenere Cipher
        vigenere_cipher = bytearray()
        for i in range(len(beaufort_cipher)):
            char_original = beaufort_cipher[i]
            char_key = key_bytes[i % len(key_bytes)]
            char_cipher = (char_original - char_key) % 256
            vigenere_cipher.append(char_cipher)

        # Create a new PIL Image from the encrypted bytes
        encrypted_image = Image.frombytes(
            "RGB", self.original_image.size, bytes(vigenere_cipher))

        # Convert PIL Image to QImage
        q_image = QImage(encrypted_image.tobytes(), encrypted_image.width, encrypted_image.height,
                         encrypted_image.width * 3, QImage.Format_RGB888)

        # Convert QImage to QPixmap
        pixmap = QPixmap.fromImage(q_image)
        self.frame_4.setPixmap(pixmap)

        # Set the encrypted image attribute
        self.encrypted_image = encrypted_image

    def save_file(self):
        if self.encrypted_image:
            file_path, _ = QFileDialog.getSaveFileName(
                self, "Save Image File", "", "Image Files (*.png *.jpg *.bmp)")
            if file_path:
                self.encrypted_image.save(file_path)


if __name__ == "__main__":
    app = QApplication([])
    window = ImageEncryptionApp()
    window.show()
    app.exec_()
