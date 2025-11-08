import sys
import os
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QListWidget,
    QFileDialog,
)
from PySide6.QtCore import Qt


class ImageViewerMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("qt 첫 실습 : 이미지 뷰")
        self.resize(600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.btn_select_folder = QPushButton("폴더 선택")
        self.btn_select_folder.clicked.connect(self.select_folder)
        layout.addWidget(self.btn_select_folder)

        self.lbl_folder_path = QLabel("선택된 폴더: (없음)")
        self.lbl_folder_path.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.lbl_folder_path)

        self.list_images = QListWidget()
        layout.addWidget(self.list_images)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "이미지 폴더 선택")
        if not folder_path:
            return
        self.lbl_folder_path.setText(f"선택된 폴더: {folder_path}")
        self.update_image_list(folder_path)

    def update_image_list(self, folder_path: str):
        self.list_images.clear()
        valid_extensions = {".jpg", ".jpeg", ".png", ".bmp"}
        for filename in os.listdir(folder_path):
            _, ext = os.path.splitext(filename)
            if ext.lower() in valid_extensions:
                self.list_images.addItem(filename)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageViewerMainWindow()
    window.show()
    app.exec()
