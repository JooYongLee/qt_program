import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt5 버튼 상태 예제')
        self.setGeometry(100, 100, 300, 200)

        # 상태값 초기화
        self.status = "초기 상태"

        # 라벨 생성
        self.label = QLabel(self.status, self)

        # 버튼 생성
        self.button = QPushButton('상태 변경하기', self)
        self.button.clicked.connect(self.change_status)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def change_status(self):
        # 상태값 변경
        print('change_status')
        self.status = "버튼이 눌렸습니다!"
        self.label.setText(self.status)  # 라벨에 상태값 표시

# 메인 실행 코드
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
