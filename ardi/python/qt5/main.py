from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageTk
import sys
class ImageEncryptionApp(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Tambahkan kode inisialisasi atau hubungkan sinyal-sinyal di sini

    def upload_image(self):
        global original_image
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            original_image = Image.open(file_path)
            original_image = original_image.resize((300, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(original_image)
            self.label_image_before.setPixmap(QPixmap(photo))

    def encrypt_image(self):
        global original_image, encrypted_image
        key = self.lineEdit.text().upper()
        key_index = 0
        encrypted_pixels = []

        # ... (kode enkripsi dari main.py)

        encrypted_image = Image.new(original_image.mode, original_image.size)
        encrypted_image.putdata(encrypted_pixels)
        encrypted_image = encrypted_image.resize((300, 200), Image.LANCZOS)

        photo = ImageTk.PhotoImage(encrypted_image)
        self.label_image_after.setPixmap(QPixmap(photo))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEncryptionApp()
    window.show()
    sys.exit(app.exec_())
